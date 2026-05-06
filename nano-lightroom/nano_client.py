"""Thin wrapper around google-genai for Nano Banana image editing."""
from __future__ import annotations

import io
from dataclasses import dataclass

from PIL import Image
from google import genai
from google.genai import types

MODEL = "gemini-2.5-flash-image"


@dataclass
class EditResult:
    image: Image.Image | None
    text: str | None
    error: str | None = None


class NanoClient:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Missing GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key)

    def edit(self, image: Image.Image, prompt: str) -> EditResult:
        """Send image + prompt to Nano Banana, return the edited image."""
        try:
            response = self.client.models.generate_content(
                model=MODEL,
                contents=[prompt, image],
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE", "TEXT"],
                ),
            )
        except Exception as exc:  # surface API errors to UI
            return EditResult(image=None, text=None, error=str(exc))

        out_image: Image.Image | None = None
        out_text: str | None = None

        candidates = getattr(response, "candidates", None) or []
        for cand in candidates:
            content = getattr(cand, "content", None)
            if not content:
                continue
            for part in getattr(content, "parts", []) or []:
                inline = getattr(part, "inline_data", None)
                if inline and getattr(inline, "data", None):
                    out_image = Image.open(io.BytesIO(inline.data))
                    out_image.load()
                elif getattr(part, "text", None):
                    out_text = (out_text or "") + part.text

        if out_image is None:
            return EditResult(
                image=None,
                text=out_text,
                error="No image returned (model may have refused or returned text only).",
            )
        return EditResult(image=out_image, text=out_text)

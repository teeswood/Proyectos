"""Image I/O helpers — preserving max quality on output."""
from __future__ import annotations

import io
from pathlib import Path

from PIL import Image, ImageOps


SUPPORTED_INPUT = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff", ".heic"}


def load_image(data: bytes) -> Image.Image:
    img = Image.open(io.BytesIO(data))
    img = ImageOps.exif_transpose(img)  # respect EXIF orientation
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGB")
    return img


def resize_to_match(graded: Image.Image, original: Image.Image) -> Image.Image:
    """Upscale the graded image back to the original resolution.

    Nano Banana caps output at ~1024px. We resize using LANCZOS so the final
    file matches the user's source resolution. The grade itself is already
    baked in at lower res; this restores pixel dimensions only.
    """
    if graded.size == original.size:
        return graded
    return graded.resize(original.size, Image.LANCZOS)


def save_bytes(
    img: Image.Image,
    fmt: str = "JPEG",
    quality: int = 100,
) -> bytes:
    """Encode image to bytes at maximum quality."""
    fmt = fmt.upper()
    buf = io.BytesIO()
    if fmt in ("JPG", "JPEG"):
        rgb = img.convert("RGB")
        rgb.save(
            buf,
            format="JPEG",
            quality=quality,
            subsampling=0,        # 4:4:4, no chroma subsampling
            optimize=True,
            progressive=True,
        )
    elif fmt == "PNG":
        img.save(buf, format="PNG", optimize=True, compress_level=6)
    elif fmt == "WEBP":
        img.save(buf, format="WEBP", quality=quality, method=6, lossless=(quality >= 100))
    elif fmt == "TIFF":
        img.save(buf, format="TIFF", compression="tiff_lzw")
    else:
        raise ValueError(f"Unsupported output format: {fmt}")
    return buf.getvalue()


def output_filename(original_name: str, preset_label: str, fmt: str) -> str:
    stem = Path(original_name).stem
    safe_label = preset_label.lower().replace(" ", "_").replace("&", "and")
    safe_label = "".join(c for c in safe_label if c.isalnum() or c in "_-")
    ext = "jpg" if fmt.upper() in ("JPG", "JPEG") else fmt.lower()
    return f"{stem}__{safe_label}.{ext}"

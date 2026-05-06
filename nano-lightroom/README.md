# Nano Lightroom 🍌

Batch photo grading powered by **Google Nano Banana** (`gemini-2.5-flash-image`). Upload a batch of photos, pick a Lightroom-style look, get the graded set back. The model is instructed to apply **only photographic color/tone adjustments** — no edits to faces, identity, anatomy, or composition.

## Features

- **Batch upload** — drop dozens of photos at once.
- **10 built-in presets** (Cinematic Teal & Orange, Bright & Airy, Kodak Portra 400, B&W Editorial, Golden Hour, Cool Nordic, Vibrant Travel, Faded Matte, Moody Earthy, Editorial Skin Tone).
- **Custom prompt override** for your own grades.
- **Identity-lock prompt prefix** — the model is repeatedly told not to alter people, faces, content, or composition.
- **Max-quality output** — JPEG q=100 with 4:4:4 chroma, PNG, WebP, or LZW TIFF.
- **Optional upscale to source resolution** — Nano Banana caps output near 1024 px; we resize back to your original dimensions with LANCZOS.
- **Side-by-side previews** + per-image download + bulk ZIP download.

## Quick start

```bash
cd nano-lightroom
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

export GEMINI_API_KEY=your_key   # or paste it in the sidebar
streamlit run app.py
```

Get an API key at <https://aistudio.google.com/apikey>.

## About "maximum quality"

Nano Banana is a **generative** model. Important caveats:

| Aspect | Behavior |
|---|---|
| Resolution | Output ~1024 px on long edge. We resample back up with LANCZOS. |
| Pixel fidelity | Not pixel-true — the model regenerates the image with the new grade. Fine details (text, hair, fabric weave) may shift subtly. |
| File quality | Saved at JPEG q=100 / 4:4:4 (no chroma subsampling), or lossless PNG/TIFF. |
| Identity preservation | Strong prompt constraints, but generative models are not 100% deterministic. Spot-check critical shots. |

If you need **pixel-true** color grading (zero subject change), traditional tools (Lightroom, Capture One, darktable, RawTherapee) remain the right choice. Nano Lightroom is best for **stylized batch looks** where a small amount of regeneration is acceptable.

## Project layout

```
nano-lightroom/
├── app.py            # Streamlit UI
├── nano_client.py    # google-genai wrapper
├── presets.py        # Lightroom-style preset prompts + identity lock
├── image_utils.py    # I/O, resize, encode
├── requirements.txt
├── .env.example
└── README.md
```

## Notes

- Each image is one API call. Batches scale linearly. Watch your quota.
- The identity-lock prefix is in `presets.py::IDENTITY_LOCK` — tweak it if you want stricter or looser constraints.
- HEIC support depends on your Pillow build; install `pillow-heif` if you need iPhone photos.

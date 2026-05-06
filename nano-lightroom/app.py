"""
Nano Lightroom — batch photo grading via Google Nano Banana
(Gemini 2.5 Flash Image).

Run:
    streamlit run app.py
"""
from __future__ import annotations

import io
import os
import time
import zipfile
from pathlib import Path

import streamlit as st
from PIL import Image


def _load_env_file() -> None:
    """Load KEY=VALUE lines from a local .env into os.environ (no extra deps)."""
    env_path = Path(__file__).with_name(".env")
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_env_file()

from image_utils import (
    SUPPORTED_INPUT,
    load_image,
    output_filename,
    resize_to_match,
    save_bytes,
)
from nano_client import NanoClient
from presets import PRESETS, build_prompt


st.set_page_config(
    page_title="Nano Lightroom",
    page_icon="🍌",
    layout="wide",
)

st.title("Nano Lightroom")
st.caption(
    "Batch photo grading powered by Google Nano Banana (Gemini 2.5 Flash Image). "
    "Applies Lightroom-style color/tone presets without altering faces, identity, "
    "or composition."
)


# ---------- sidebar ----------
with st.sidebar:
    st.header("⚙️ Settings")

    api_key = st.text_input(
        "Gemini API key",
        value=os.getenv("GEMINI_API_KEY", ""),
        type="password",
        help="Get one at https://aistudio.google.com/apikey",
    )

    st.divider()
    st.subheader("🎨 Look")

    preset_names = list(PRESETS.keys())
    preset_name = st.selectbox(
        "Preset",
        preset_names,
        index=0,
    )
    st.caption(PRESETS[preset_name]["description"])

    use_custom = st.checkbox("Override with custom prompt")
    custom_prompt = ""
    if use_custom:
        custom_prompt = st.text_area(
            "Custom grade description",
            placeholder="e.g. cool desaturated cyberpunk grade with magenta highlights…",
            height=120,
        )

    st.divider()
    st.subheader("💾 Output")

    out_format = st.selectbox("Format", ["JPEG", "PNG", "WEBP", "TIFF"], index=0)
    quality = st.slider(
        "Quality",
        min_value=70,
        max_value=100,
        value=100,
        help="JPEG/WebP quality. PNG/TIFF ignore this.",
    )
    upscale_to_original = st.checkbox(
        "Upscale output to original resolution",
        value=True,
        help=(
            "Nano Banana returns ~1024px images. Enable this to resize the graded "
            "result back to the source resolution using LANCZOS resampling."
        ),
    )

    st.divider()
    with st.expander("ℹ️ About max quality"):
        st.markdown(
            "- Nano Banana outputs at roughly **1024 px** on the long edge.\n"
            "- We resize back to your original resolution and save at "
            "**JPEG q=100, 4:4:4** (no chroma subsampling) — so file quality is "
            "max, but pixel-level detail is what the model returned.\n"
            "- For pixel-true detail preservation use a traditional grader; "
            "Nano Banana is generative."
        )


# ---------- uploader ----------
uploaded = st.file_uploader(
    "Drop photos here (batch supported)",
    type=[ext.strip(".") for ext in SUPPORTED_INPUT],
    accept_multiple_files=True,
)

col_a, col_b = st.columns([1, 4])
with col_a:
    run = st.button(
        "🚀 Process batch",
        type="primary",
        disabled=not uploaded or not api_key,
    )
with col_b:
    if not api_key:
        st.warning("Add your Gemini API key in the sidebar.")
    elif not uploaded:
        st.info("Upload one or more photos to begin.")


# ---------- processing ----------
if run and uploaded and api_key:
    try:
        client = NanoClient(api_key)
    except Exception as exc:
        st.error(f"Could not initialize client: {exc}")
        st.stop()

    prompt = build_prompt(preset_name, custom_prompt if use_custom else None)
    label = "custom" if (use_custom and custom_prompt.strip()) else preset_name

    with st.expander("🔍 Prompt being sent"):
        st.code(prompt, language="markdown")

    progress = st.progress(0.0, text="Starting…")
    results: list[tuple[str, bytes, Image.Image, Image.Image]] = []
    errors: list[tuple[str, str]] = []

    total = len(uploaded)
    started = time.time()

    for idx, file in enumerate(uploaded, start=1):
        progress.progress(
            (idx - 1) / total,
            text=f"[{idx}/{total}] {file.name} — sending to Nano Banana…",
        )

        try:
            original = load_image(file.getvalue())
        except Exception as exc:
            errors.append((file.name, f"Could not read: {exc}"))
            continue

        result = client.edit(original, prompt)
        if result.error or result.image is None:
            errors.append((file.name, result.error or "Unknown error"))
            continue

        graded = result.image
        if upscale_to_original:
            graded = resize_to_match(graded, original)

        encoded = save_bytes(graded, fmt=out_format, quality=quality)
        out_name = output_filename(file.name, label, out_format)
        results.append((out_name, encoded, original, graded))

    progress.progress(1.0, text=f"Done in {time.time() - started:.1f}s")

    # ---------- gallery ----------
    if results:
        st.success(f"Processed {len(results)}/{total} photos.")

        # ZIP for download
        zip_buf = io.BytesIO()
        with zipfile.ZipFile(zip_buf, "w", zipfile.ZIP_STORED) as zf:
            for name, data, _, _ in results:
                zf.writestr(name, data)
        st.download_button(
            "⬇️ Download all (ZIP)",
            data=zip_buf.getvalue(),
            file_name=f"nano_lightroom_{label.replace(' ', '_')}.zip",
            mime="application/zip",
        )

        st.divider()
        st.subheader("Previews")
        for name, data, original, graded in results:
            with st.container(border=True):
                st.markdown(f"**{name}** — {graded.size[0]}×{graded.size[1]} px")
                c1, c2 = st.columns(2)
                with c1:
                    st.caption("Original")
                    st.image(original, use_container_width=True)
                with c2:
                    st.caption(f"Graded · {label}")
                    st.image(graded, use_container_width=True)
                st.download_button(
                    f"Download {name}",
                    data=data,
                    file_name=name,
                    mime=f"image/{'jpeg' if out_format.upper() == 'JPEG' else out_format.lower()}",
                    key=f"dl-{name}",
                )

    if errors:
        st.divider()
        with st.expander(f"⚠️ {len(errors)} error(s)"):
            for name, err in errors:
                st.write(f"- **{name}** — {err}")

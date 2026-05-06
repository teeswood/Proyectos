"""Deterministic Lightroom-style color grader (Pillow + numpy).

Pure pixel ops — exposure, white balance, tone, contrast, HSL, color grade,
saturation, vibrance, B&W mix, grain. No generative steps; geometry is never
touched, so identity is preserved by construction.
"""
from __future__ import annotations

import numpy as np
from PIL import Image


# ---------- conversions ----------

def _to_array(img: Image.Image) -> np.ndarray:
    if img.mode != "RGB":
        img = img.convert("RGB")
    return np.asarray(img, dtype=np.float32) / 255.0


def _from_array(arr: np.ndarray) -> Image.Image:
    arr = np.clip(arr, 0.0, 1.0)
    return Image.fromarray((arr * 255.0 + 0.5).astype(np.uint8), "RGB")


def _srgb_to_linear(c: np.ndarray) -> np.ndarray:
    c = np.maximum(c, 0.0)
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def _linear_to_srgb(c: np.ndarray) -> np.ndarray:
    c = np.maximum(c, 0.0)
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * (c ** (1.0 / 2.4)) - 0.055)


def _luma(arr: np.ndarray) -> np.ndarray:
    return 0.2126 * arr[..., 0] + 0.7152 * arr[..., 1] + 0.0722 * arr[..., 2]


def _smoothstep(x: np.ndarray, a: float, b: float) -> np.ndarray:
    t = np.clip((x - a) / (b - a + 1e-9), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def _rgb_to_hsv(arr: np.ndarray) -> np.ndarray:
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    mx = np.max(arr, axis=-1)
    mn = np.min(arr, axis=-1)
    df = mx - mn
    df_safe = np.where(df == 0, 1.0, df)
    rc = (mx - r) / df_safe
    gc = (mx - g) / df_safe
    bc = (mx - b) / df_safe
    h = np.where(
        mx == r, (bc - gc),
        np.where(mx == g, 2.0 + rc - bc, 4.0 + gc - rc),
    )
    h = (h / 6.0) % 1.0
    h = np.where(df == 0, 0.0, h)
    s = np.where(mx == 0, 0.0, df / np.where(mx == 0, 1.0, mx))
    return np.stack([h, s, mx], axis=-1)


def _hsv_to_rgb(arr: np.ndarray) -> np.ndarray:
    h, s, v = arr[..., 0], arr[..., 1], arr[..., 2]
    h6 = (h % 1.0) * 6.0
    i = np.floor(h6).astype(np.int32)
    f = h6 - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i_mod = i % 6
    r = np.choose(i_mod, [v, q, p, p, t, v])
    g = np.choose(i_mod, [t, v, v, q, p, p])
    b = np.choose(i_mod, [p, p, t, v, v, q])
    return np.stack([r, g, b], axis=-1)


# ---------- ops ----------

def _op_exposure(arr: np.ndarray, stops: float) -> np.ndarray:
    if not stops:
        return arr
    lin = _srgb_to_linear(arr)
    lin = lin * (2.0 ** float(stops))
    return _linear_to_srgb(lin)


def _op_white_balance(arr: np.ndarray, temp: float, tint: float) -> np.ndarray:
    if not temp and not tint:
        return arr
    t = float(temp or 0) / 60.0
    g = float(tint or 0) / 60.0
    r_mul = 1.0 + 0.5 * t
    b_mul = 1.0 - 0.5 * t
    g_mul = 1.0 - 0.4 * g
    lin = _srgb_to_linear(arr)
    lin = lin.copy()
    lin[..., 0] *= r_mul
    lin[..., 1] *= g_mul
    lin[..., 2] *= b_mul
    return _linear_to_srgb(lin)


def _op_tone(arr: np.ndarray, shadows: float, highlights: float,
             whites: float, blacks: float) -> np.ndarray:
    if not any([shadows, highlights, whites, blacks]):
        return arr
    L = _luma(arr)
    m_shadow = 1.0 - _smoothstep(L, 0.0, 0.5)
    m_high = _smoothstep(L, 0.5, 1.0)
    m_blacks = 1.0 - _smoothstep(L, 0.0, 0.25)
    m_whites = _smoothstep(L, 0.75, 1.0)

    delta = np.zeros_like(L)
    if shadows:
        delta += (float(shadows) / 100.0) * 0.5 * m_shadow
    if highlights:
        delta += (float(highlights) / 100.0) * 0.5 * m_high
    if blacks:
        delta += (float(blacks) / 100.0) * 0.4 * m_blacks
    if whites:
        delta += (float(whites) / 100.0) * 0.4 * m_whites

    return arr + delta[..., None]


def _op_contrast(arr: np.ndarray, amount: float) -> np.ndarray:
    if not amount:
        return arr
    k = float(amount) / 100.0
    if k > 0:
        scale = 1.0 + 5.0 * k
        return 0.5 + np.tanh((arr - 0.5) * scale) / (2.0 * np.tanh(0.5 * scale))
    return 0.5 + (arr - 0.5) * (1.0 + 0.7 * k)  # k<0 → flatten


_HSL_CENTERS = {
    "red": 0.0,
    "orange": 30.0,
    "yellow": 60.0,
    "green": 120.0,
    "aqua": 180.0,
    "blue": 240.0,
    "purple": 270.0,
    "magenta": 300.0,
}
_HSL_SIGMA = 30.0


def _hsl_weights(h_deg: np.ndarray, center: float) -> np.ndarray:
    d = np.abs(((h_deg - center + 180.0) % 360.0) - 180.0)
    return np.exp(-(d * d) / (2.0 * _HSL_SIGMA * _HSL_SIGMA))


def _op_hsl(arr: np.ndarray, hsl: dict | None) -> np.ndarray:
    if not hsl:
        return arr
    hsv = _rgb_to_hsv(arr)
    h_deg = hsv[..., 0] * 360.0
    s = hsv[..., 1]
    v = hsv[..., 2]
    sat_mask = np.clip(s, 0.0, 1.0)

    dh = np.zeros_like(h_deg)
    ds = np.zeros_like(s)
    dl = np.zeros_like(v)

    for color, params in hsl.items():
        center = _HSL_CENTERS.get(color)
        if center is None:
            continue
        w = _hsl_weights(h_deg, center) * sat_mask
        dh += w * float(params.get("h", 0))
        ds += w * (float(params.get("s", 0)) / 100.0)
        dl += w * (float(params.get("l", 0)) / 100.0)

    h_new = ((h_deg + dh) % 360.0) / 360.0
    s_new = np.clip(s * (1.0 + ds), 0.0, 1.0)
    v_new = np.clip(v * (1.0 + dl * 0.5), 0.0, 1.0)
    return _hsv_to_rgb(np.stack([h_new, s_new, v_new], axis=-1))


_CG_REGIONS = ("shadows", "midtones", "highlights")


def _op_color_grade(arr: np.ndarray, cg: dict | None) -> np.ndarray:
    if not cg:
        return arr
    L = _luma(arr)
    m_shadow = 1.0 - _smoothstep(L, 0.0, 0.5)
    m_high = _smoothstep(L, 0.5, 1.0)
    m_mid = (1.0 - m_shadow) * (1.0 - m_high)
    masks = {"shadows": m_shadow, "midtones": m_mid, "highlights": m_high}

    out = arr
    for region, params in cg.items():
        if region not in masks:
            continue
        sat = float(params.get("sat", 0)) / 100.0
        if sat == 0:
            continue
        hue = float(params.get("hue", 0)) / 360.0
        tint = _hsv_to_rgb(np.array([[[hue % 1.0, 1.0, 1.0]]], dtype=np.float32))[0, 0]
        weight = (masks[region] * sat * 0.4)[..., None]
        out = out + (tint - 0.5) * weight
    return out


def _op_saturation(arr: np.ndarray, amount: float) -> np.ndarray:
    if not amount:
        return arr
    hsv = _rgb_to_hsv(arr)
    hsv = hsv.copy()
    hsv[..., 1] = np.clip(hsv[..., 1] * (1.0 + float(amount) / 100.0), 0.0, 1.0)
    return _hsv_to_rgb(hsv)


def _op_vibrance(arr: np.ndarray, amount: float) -> np.ndarray:
    if not amount:
        return arr
    hsv = _rgb_to_hsv(arr)
    s = hsv[..., 1]
    h_deg = hsv[..., 0] * 360.0
    skin = np.exp(-((h_deg - 25.0) ** 2) / (2.0 * 20.0 * 20.0))
    protect = (1.0 - s) * (1.0 - 0.5 * skin)
    s_new = np.clip(s + (float(amount) / 100.0) * protect, 0.0, 1.0)
    hsv = hsv.copy()
    hsv[..., 1] = s_new
    return _hsv_to_rgb(hsv)


def _op_bw_mix(arr: np.ndarray, mix) -> np.ndarray:
    if not mix:
        return arr
    r_w, g_w, b_w = mix
    L = arr[..., 0] * float(r_w) + arr[..., 1] * float(g_w) + arr[..., 2] * float(b_w)
    return np.stack([L, L, L], axis=-1)


def _op_grain(arr: np.ndarray, amount: float) -> np.ndarray:
    if not amount:
        return arr
    sigma = (float(amount) / 100.0) * 0.1
    h, w = arr.shape[:2]
    noise = np.random.normal(0.0, sigma, (h, w)).astype(np.float32)
    return arr + noise[..., None]


# ---------- public ----------

def apply(image: Image.Image, ops: dict | None) -> Image.Image:
    """Apply a color-grading ops dict to a PIL image and return a new PIL image."""
    if not ops:
        return image
    arr = _to_array(image)
    arr = _op_exposure(arr, ops.get("exposure", 0))
    arr = _op_white_balance(arr, ops.get("temp", 0), ops.get("tint", 0))
    arr = _op_tone(
        arr,
        ops.get("shadows", 0),
        ops.get("highlights", 0),
        ops.get("whites", 0),
        ops.get("blacks", 0),
    )
    arr = _op_contrast(arr, ops.get("contrast", 0))
    arr = _op_hsl(arr, ops.get("hsl"))
    arr = _op_color_grade(arr, ops.get("color_grade"))
    arr = _op_saturation(arr, ops.get("saturation", 0))
    arr = _op_vibrance(arr, ops.get("vibrance", 0))
    arr = _op_bw_mix(arr, ops.get("bw_mix"))
    arr = _op_grain(arr, ops.get("grain", 0))
    return _from_array(arr)

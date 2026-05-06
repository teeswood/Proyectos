"""
Lightroom-style presets for Nano Banana (Gemini 2.5 Flash Image).

Each preset is a prompt that instructs the model to apply ONLY photographic
color/tone adjustments — no edits to faces, anatomy, composition, content,
people, objects, or background structure.
"""

IDENTITY_LOCK = (
    "STRICT RULES — apply ONLY photographic color and tonal adjustments. "
    "Do NOT alter faces, skin features, body proportions, identity, hair, clothing, "
    "objects, text, composition, framing, perspective, or background content. "
    "Do NOT add, remove, or move any element. Do NOT change facial expressions. "
    "Preserve every pixel of subject geometry — only the color/light response changes. "
    "Treat the input strictly as a RAW photograph being graded in a non-destructive editor "
    "(like Lightroom): adjust only exposure, contrast, white balance, highlights, shadows, "
    "whites, blacks, saturation, vibrance, hue shifts, tone curves, split toning, and grain."
)


PRESETS: dict[str, dict] = {
    "Cinematic Teal & Orange": {
        "description": "Skin warm orange, shadows pushed to teal. Wide tonal range, slight contrast lift.",
        "prompt": (
            "Apply a CINEMATIC TEAL & ORANGE color grade. "
            "Push shadows toward teal/cyan, lift highlights and midtone skin tones toward warm orange. "
            "Slightly increase contrast, gentle S-curve, mild desaturation of greens, "
            "subtle film-like roll-off in highlights. Skin remains natural and warm. "
            "Keep luminance balanced; this is a Hollywood color grade, not an Instagram filter."
        ),
        "ops": {
            "contrast": 12,
            "hsl": {
                "orange": {"h": -3, "s": 8, "l": 3},
                "blue":   {"s": 10, "l": -5},
                "green":  {"s": -15},
            },
            "color_grade": {
                "shadows":    {"hue": 195, "sat": 18},
                "highlights": {"hue": 30,  "sat": 12},
            },
        },
    },
    "Moody Dark & Earthy": {
        "description": "Deep shadows, muted greens, desaturated tones, autumnal palette.",
        "prompt": (
            "Apply a MOODY DARK & EARTHY look. "
            "Crush blacks slightly, lower exposure 1/3 stop, desaturate overall, "
            "shift greens toward olive/khaki, oranges toward terracotta, "
            "blues toward muted slate. Add subtle warmth in shadows, cool highlights. "
            "Result feels overcast, autumnal, editorial."
        ),
        "ops": {
            "exposure": -0.3,
            "saturation": -15,
            "blacks": -8,
            "hsl": {
                "green":  {"h": -10, "s": -15, "l": -5},
                "orange": {"h": -5,  "s": -10},
                "blue":   {"s": -20, "l": -5},
            },
            "color_grade": {
                "shadows":    {"hue": 30,  "sat": 6},
                "highlights": {"hue": 200, "sat": 6},
            },
        },
    },
    "Bright & Airy": {
        "description": "Light, soft, low-contrast wedding/lifestyle look.",
        "prompt": (
            "Apply a BRIGHT & AIRY look. "
            "Increase exposure ~1/2 stop, lift shadows significantly, soften contrast, "
            "raise whites, pull highlights down slightly to retain detail. "
            "Slight pastel tint: gentle pink in highlights, soft cream in midtones. "
            "Slightly desaturate to keep tones soft. Pure clean whites preserved."
        ),
        "ops": {
            "exposure": 0.4,
            "shadows": 30,
            "highlights": -15,
            "whites": 8,
            "contrast": -8,
            "saturation": -10,
            "color_grade": {
                "highlights": {"hue": 350, "sat": 6},
            },
        },
    },
    "Vintage Film (Kodak Portra 400)": {
        "description": "Warm, slightly faded, film-like grain, classic skin rendering.",
        "prompt": (
            "Emulate KODAK PORTRA 400 35mm film. "
            "Warm white balance, slightly green-shifted shadows, creamy skin tones, "
            "gentle highlight roll-off, lifted blacks (raised toe), reduced contrast, "
            "soft grain, mild halation around bright areas. Saturation natural-low, "
            "yellows slightly muted, reds rich but not punchy."
        ),
        "ops": {
            "temp": 8,
            "blacks": 12,
            "contrast": -6,
            "highlights": -8,
            "hsl": {
                "yellow": {"l": 8, "s": -5},
                "red":    {"s": 8},
                "green":  {"h": -8},
            },
            "grain": 6,
        },
    },
    "Black & White Editorial": {
        "description": "High-contrast monochrome with rich tonal separation.",
        "prompt": (
            "Convert to BLACK & WHITE EDITORIAL. "
            "Use a panchromatic conversion with red channel slightly boosted for skin glow. "
            "Deep blacks, clean whites, strong but controlled contrast, preserve midtone detail. "
            "Subtle film grain. No tinting — pure neutral monochrome."
        ),
        "ops": {
            "contrast": 18,
            "blacks": -10,
            "whites": 5,
            "bw_mix": (0.42, 0.40, 0.18),
            "grain": 5,
        },
    },
    "Warm Golden Hour": {
        "description": "Sun-soaked, warm highlights, glowing skin.",
        "prompt": (
            "Apply a WARM GOLDEN HOUR look. "
            "Shift white balance warmer (+10 mireds), boost orange and yellow saturation slightly, "
            "warm highlights, add soft amber tint to overall image, lift shadows gently. "
            "Skin glows, light feels low and golden. Avoid orange-cast on whites — keep paper white."
        ),
        "ops": {
            "temp": 12,
            "shadows": 12,
            "hsl": {
                "orange": {"s": 10, "l": 4},
                "yellow": {"s": 10},
            },
            "color_grade": {
                "highlights": {"hue": 35, "sat": 14},
            },
        },
    },
    "Cool Nordic": {
        "description": "Cool blue tones, crisp shadows, desaturated palette.",
        "prompt": (
            "Apply a COOL NORDIC look. "
            "Cool white balance (-10 mireds), shift shadows toward blue, "
            "desaturate oranges and reds, keep greens slightly muted, "
            "increase clarity subtly, deepen blacks. Crisp, clean, slightly cinematic."
        ),
        "ops": {
            "temp": -10,
            "blacks": -8,
            "contrast": 6,
            "hsl": {
                "orange": {"s": -15},
                "red":    {"s": -10},
                "green":  {"s": -8},
            },
            "color_grade": {
                "shadows": {"hue": 220, "sat": 12},
            },
        },
    },
    "Vibrant Travel": {
        "description": "Punchy, saturated, high-clarity travel/landscape look.",
        "prompt": (
            "Apply a VIBRANT TRAVEL look. "
            "Boost vibrance more than saturation, increase clarity/structure moderately, "
            "deepen blue skies (HSL: blue luminance down, saturation up), enrich greens, "
            "add subtle contrast S-curve. Skin tones protected — only environmental colors pop."
        ),
        "ops": {
            "contrast": 10,
            "vibrance": 25,
            "hsl": {
                "blue":  {"s": 18, "l": -8},
                "green": {"s": 15},
            },
        },
    },
    "Faded Matte": {
        "description": "Lifted blacks, low contrast, modern Instagram-matte look.",
        "prompt": (
            "Apply a FADED MATTE look. "
            "Lift blacks significantly (raised toe), pull highlights down, "
            "lower overall contrast, slight cyan tint in shadows, slight peach in highlights. "
            "Desaturated overall. Modern, flat, social-media editorial."
        ),
        "ops": {
            "blacks": 25,
            "highlights": -10,
            "contrast": -15,
            "saturation": -12,
            "color_grade": {
                "shadows":    {"hue": 190, "sat": 10},
                "highlights": {"hue": 25,  "sat": 8},
            },
        },
    },
    "High-End Skin Retouch Tone": {
        "description": "Magazine-style clean skin tone grading (no actual retouching).",
        "prompt": (
            "Apply a HIGH-END EDITORIAL skin-tone grade — color/tone only, do NOT smooth, "
            "blur, or alter skin texture or features. "
            "Neutralize color casts on skin, slightly desaturate reds in skin range, "
            "balance highlights toward neutral, deepen blacks, gentle contrast, "
            "luminous midtones. Background slightly desaturated to draw eye to subject."
        ),
        "ops": {
            "contrast": 5,
            "blacks": -8,
            "saturation": -8,
            "hsl": {
                "red":    {"s": -12},
                "orange": {"s": -8, "l": 3},
            },
        },
    },
}


def build_prompt(preset_name: str, custom_prompt: str | None = None) -> str:
    """Combine identity-lock instructions with the chosen preset (or a custom prompt)."""
    if custom_prompt and custom_prompt.strip():
        body = custom_prompt.strip()
    else:
        body = PRESETS[preset_name]["prompt"]
    return f"{IDENTITY_LOCK}\n\nGRADE TO APPLY:\n{body}"

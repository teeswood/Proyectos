// Lightroom-style presets for Nano Banana (Gemini 2.5 Flash Image).
// Each preset is a prompt that instructs the model to apply ONLY photographic
// color/tone adjustments — no edits to faces, anatomy, composition, or content.

export const IDENTITY_LOCK =
  'STRICT RULES — apply ONLY photographic color and tonal adjustments. ' +
  'Do NOT alter faces, skin features, body proportions, identity, hair, clothing, ' +
  'objects, text, composition, framing, perspective, or background content. ' +
  'Do NOT add, remove, or move any element. Do NOT change facial expressions. ' +
  'Preserve every pixel of subject geometry — only the color/light response changes. ' +
  'Treat the input strictly as a RAW photograph being graded in a non-destructive editor ' +
  '(like Lightroom): adjust only exposure, contrast, white balance, highlights, shadows, ' +
  'whites, blacks, saturation, vibrance, hue shifts, tone curves, split toning, and grain.';

export const PRESETS = [
  {
    id: 'cinematic',
    name: 'Cinematic Teal & Orange',
    description: 'Skin warm orange, shadows pushed to teal. Wide tonal range.',
    prompt:
      'Apply a CINEMATIC TEAL & ORANGE color grade. Push shadows toward teal/cyan, ' +
      'lift highlights and midtone skin tones toward warm orange. Slightly increase ' +
      'contrast, gentle S-curve, mild desaturation of greens, subtle film-like roll-off ' +
      'in highlights. Skin remains natural and warm.',
  },
  {
    id: 'moody',
    name: 'Moody Dark & Earthy',
    description: 'Deep shadows, muted greens, autumnal palette.',
    prompt:
      'Apply a MOODY DARK & EARTHY look. Crush blacks slightly, lower exposure ~1/3 stop, ' +
      'desaturate overall, shift greens toward olive/khaki, oranges toward terracotta, ' +
      'blues toward muted slate. Result feels overcast, autumnal, editorial.',
  },
  {
    id: 'airy',
    name: 'Bright & Airy',
    description: 'Light, soft, low-contrast wedding/lifestyle look.',
    prompt:
      'Apply a BRIGHT & AIRY look. Increase exposure ~1/2 stop, lift shadows significantly, ' +
      'soften contrast, raise whites, pull highlights down slightly. Slight pastel tint: ' +
      'gentle pink in highlights, soft cream in midtones. Slightly desaturated.',
  },
  {
    id: 'portra',
    name: 'Kodak Portra 400',
    description: 'Warm, faded, film-like grain, classic skin rendering.',
    prompt:
      'Emulate KODAK PORTRA 400 35mm film. Warm white balance, slightly green-shifted shadows, ' +
      'creamy skin tones, gentle highlight roll-off, lifted blacks, reduced contrast, ' +
      'soft grain, mild halation. Saturation natural-low, yellows muted, reds rich but not punchy.',
  },
  {
    id: 'bw',
    name: 'Black & White Editorial',
    description: 'High-contrast monochrome, rich tonal separation.',
    prompt:
      'Convert to BLACK & WHITE EDITORIAL. Use a panchromatic conversion with red channel ' +
      'slightly boosted for skin glow. Deep blacks, clean whites, strong but controlled ' +
      'contrast, preserve midtone detail. Subtle film grain. No tinting — pure neutral monochrome.',
  },
  {
    id: 'golden',
    name: 'Warm Golden Hour',
    description: 'Sun-soaked, warm highlights, glowing skin.',
    prompt:
      'Apply a WARM GOLDEN HOUR look. Shift white balance warmer, boost orange and yellow ' +
      'saturation slightly, warm highlights, add soft amber tint, lift shadows gently. ' +
      'Skin glows. Avoid orange-cast on whites — keep paper white.',
  },
  {
    id: 'nordic',
    name: 'Cool Nordic',
    description: 'Cool blue tones, crisp shadows, desaturated palette.',
    prompt:
      'Apply a COOL NORDIC look. Cool white balance, shift shadows toward blue, ' +
      'desaturate oranges and reds, keep greens slightly muted, increase clarity subtly, ' +
      'deepen blacks. Crisp, clean, slightly cinematic.',
  },
  {
    id: 'vibrant',
    name: 'Vibrant Travel',
    description: 'Punchy, saturated, high-clarity travel/landscape look.',
    prompt:
      'Apply a VIBRANT TRAVEL look. Boost vibrance more than saturation, increase clarity ' +
      'moderately, deepen blue skies (HSL: blue luminance down, saturation up), enrich greens, ' +
      'add subtle contrast S-curve. Skin tones protected — only environmental colors pop.',
  },
  {
    id: 'matte',
    name: 'Faded Matte',
    description: 'Lifted blacks, low contrast, modern matte look.',
    prompt:
      'Apply a FADED MATTE look. Lift blacks significantly, pull highlights down, lower ' +
      'overall contrast, slight cyan tint in shadows, slight peach in highlights. ' +
      'Desaturated overall. Modern, flat, social-media editorial.',
  },
  {
    id: 'editorial',
    name: 'Editorial Skin Tone',
    description: 'Magazine-style clean skin tone grading (no retouching).',
    prompt:
      'Apply a HIGH-END EDITORIAL skin-tone grade — color/tone only, do NOT smooth, blur, ' +
      'or alter skin texture or features. Neutralize color casts on skin, slightly desaturate ' +
      'reds in skin range, balance highlights toward neutral, deepen blacks, gentle contrast, ' +
      'luminous midtones.',
  },
];

export function buildPrompt(preset, customPrompt) {
  const body = customPrompt && customPrompt.trim() ? customPrompt.trim() : preset.prompt;
  return `${IDENTITY_LOCK}\n\nGRADE TO APPLY:\n${body}`;
}

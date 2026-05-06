// Direct REST call to the Gemini Nano Banana endpoint.
// We use fetch instead of @google/genai because the SDK depends on Node APIs
// that aren't available in React Native.

const MODEL = 'gemini-2.5-flash-image';
const ENDPOINT = `https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent`;

/**
 * Edit a single image with Nano Banana.
 *
 * @param {string} apiKey
 * @param {string} prompt
 * @param {string} base64Image  raw base64 string (no data: prefix)
 * @param {string} mimeType     e.g. 'image/jpeg'
 * @returns {Promise<{ base64: string, mimeType: string, text: string | null }>}
 */
export async function editImage(apiKey, prompt, base64Image, mimeType = 'image/jpeg') {
  if (!apiKey) throw new Error('Missing Gemini API key');

  const body = {
    contents: [
      {
        parts: [
          { text: prompt },
          { inline_data: { mime_type: mimeType, data: base64Image } },
        ],
      },
    ],
    generationConfig: {
      responseModalities: ['IMAGE', 'TEXT'],
    },
  };

  const response = await fetch(`${ENDPOINT}?key=${apiKey}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });

  if (!response.ok) {
    const errText = await response.text();
    throw new Error(`Gemini API ${response.status}: ${errText.slice(0, 300)}`);
  }

  const json = await response.json();
  const parts = json?.candidates?.[0]?.content?.parts ?? [];

  let imagePart = null;
  let text = null;
  for (const part of parts) {
    if (part.inline_data?.data || part.inlineData?.data) {
      imagePart = part.inline_data ?? part.inlineData;
    } else if (part.text) {
      text = (text ?? '') + part.text;
    }
  }

  if (!imagePart) {
    throw new Error(text ? `Model returned text only: ${text.slice(0, 200)}` : 'No image in response');
  }

  return {
    base64: imagePart.data,
    mimeType: imagePart.mime_type ?? imagePart.mimeType ?? 'image/png',
    text,
  };
}

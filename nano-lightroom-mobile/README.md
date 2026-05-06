# Nano Lightroom — Mobile (Expo)

iOS/Android version of Nano Lightroom. Pick a batch of photos, apply a Lightroom-style preset, save back to your camera roll. All processing goes through Google Nano Banana (`gemini-2.5-flash-image`) directly from your device.

## Run on your iPhone (no Mac needed)

1. Install **Expo Go** from the App Store on your iPhone.
2. On your laptop:
   ```bash
   cd nano-lightroom-mobile
   npm install
   npx expo start
   ```
3. Scan the QR code shown in the terminal with your iPhone camera. Expo Go will open the app.
4. Tap the gear icon, paste your Gemini API key (get one at <https://aistudio.google.com/apikey>). The key is stored in iOS Keychain via `expo-secure-store` — it never leaves your device or this codebase.
5. Pick photos → choose a preset → **Process**. Press-and-hold on a result to compare against the original.

Your laptop and phone must be on the same Wi-Fi. If not, run `npx expo start --tunnel`.

## Build a standalone IPA (optional, requires Apple Developer)

```bash
npm install -g eas-cli
eas login
eas build -p ios --profile preview
```

This produces an `.ipa` you can install via TestFlight or sideload. Requires an Apple Developer account ($99/year).

## Caveats

- Nano Banana is **generative**: output is regenerated near 1024 px. The native app does not currently upscale back to source resolution — add an upscale step if you need full-res output (e.g. via a Sharp-on-server function or a native image library).
- API costs apply per request. Each photo in the batch is one API call.
- The identity-lock prompt prefix in `lib/presets.js` strongly constrains the model to color/tone changes only, but generative models are not 100% deterministic. Spot-check critical photos.

## Project layout

```
nano-lightroom-mobile/
├── App.js              # main screen + settings modal
├── app.json            # Expo config (iOS permissions, plugins)
├── babel.config.js
├── package.json
└── lib/
    ├── presets.js      # Lightroom-style preset prompts + identity lock
    ├── nanoClient.js   # REST call to Gemini
    └── storage.js      # SecureStore wrapper for API key
```

// Tiny wrapper around expo-secure-store for the Gemini API key.
import * as SecureStore from 'expo-secure-store';

const KEY = 'gemini_api_key';

export async function getApiKey() {
  try {
    return await SecureStore.getItemAsync(KEY);
  } catch {
    return null;
  }
}

export async function setApiKey(value) {
  if (!value) {
    await SecureStore.deleteItemAsync(KEY);
    return;
  }
  await SecureStore.setItemAsync(KEY, value);
}

export async function clearApiKey() {
  await SecureStore.deleteItemAsync(KEY);
}

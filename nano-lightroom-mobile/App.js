import { useEffect, useState } from 'react';
import {
  ActivityIndicator,
  Alert,
  FlatList,
  Image,
  Modal,
  Pressable,
  ScrollView,
  StyleSheet,
  Text,
  TextInput,
  View,
} from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { SafeAreaProvider, SafeAreaView } from 'react-native-safe-area-context';
import * as ImagePicker from 'expo-image-picker';
import * as MediaLibrary from 'expo-media-library';
import * as FileSystem from 'expo-file-system';

import { PRESETS, buildPrompt } from './lib/presets';
import { editImage } from './lib/nanoClient';
import { getApiKey, setApiKey } from './lib/storage';

export default function App() {
  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.root} edges={['top', 'left', 'right']}>
        <StatusBar style="light" />
        <Main />
      </SafeAreaView>
    </SafeAreaProvider>
  );
}

function Main() {
  const [apiKey, setApiKeyState] = useState(null);
  const [apiKeyLoaded, setApiKeyLoaded] = useState(false);
  const [settingsOpen, setSettingsOpen] = useState(false);
  const [selectedPreset, setSelectedPreset] = useState(PRESETS[0]);
  const [photos, setPhotos] = useState([]);          // picker assets
  const [results, setResults] = useState([]);        // { id, originalUri, gradedUri, error }
  const [progress, setProgress] = useState(null);    // { current, total }

  useEffect(() => {
    (async () => {
      const stored = await getApiKey();
      setApiKeyState(stored);
      setApiKeyLoaded(true);
      if (!stored) setSettingsOpen(true);
    })();
  }, []);

  const pickPhotos = async () => {
    const perm = await ImagePicker.requestMediaLibraryPermissionsAsync();
    if (!perm.granted) {
      Alert.alert('Permission needed', 'Photo library access is required.');
      return;
    }
    const res = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ['images'],
      allowsMultipleSelection: true,
      selectionLimit: 0,
      quality: 1,
      base64: false,
    });
    if (!res.canceled && res.assets?.length) {
      setPhotos(res.assets);
      setResults([]);
    }
  };

  const processBatch = async () => {
    if (!apiKey) {
      setSettingsOpen(true);
      return;
    }
    if (!photos.length) return;

    const prompt = buildPrompt(selectedPreset, null);
    setResults([]);
    setProgress({ current: 0, total: photos.length });

    const out = [];
    for (let i = 0; i < photos.length; i++) {
      const asset = photos[i];
      setProgress({ current: i, total: photos.length });

      try {
        const base64 = await FileSystem.readAsStringAsync(asset.uri, {
          encoding: FileSystem.EncodingType.Base64,
        });
        const mime = guessMime(asset.fileName, asset.mimeType);

        const edited = await editImage(apiKey, prompt, base64, mime);

        const ext = edited.mimeType.includes('png') ? 'png' : 'jpg';
        const fname = `nano_${Date.now()}_${i}.${ext}`;
        const localUri = FileSystem.documentDirectory + fname;
        await FileSystem.writeAsStringAsync(localUri, edited.base64, {
          encoding: FileSystem.EncodingType.Base64,
        });

        out.push({
          id: `${asset.assetId ?? asset.uri}-${i}`,
          originalUri: asset.uri,
          gradedUri: localUri,
          error: null,
        });
      } catch (err) {
        out.push({
          id: `${asset.assetId ?? asset.uri}-${i}`,
          originalUri: asset.uri,
          gradedUri: null,
          error: err.message ?? String(err),
        });
      }

      setResults([...out]);
    }
    setProgress(null);
  };

  const saveAllToPhotos = async () => {
    const perm = await MediaLibrary.requestPermissionsAsync();
    if (!perm.granted) {
      Alert.alert('Permission needed', 'Allow saving to your camera roll.');
      return;
    }
    let saved = 0;
    for (const r of results) {
      if (!r.gradedUri) continue;
      try {
        await MediaLibrary.saveToLibraryAsync(r.gradedUri);
        saved += 1;
      } catch {
        // ignore individual failures
      }
    }
    Alert.alert('Saved', `${saved} photo${saved === 1 ? '' : 's'} saved to your library.`);
  };

  const saveOne = async (uri) => {
    const perm = await MediaLibrary.requestPermissionsAsync();
    if (!perm.granted) {
      Alert.alert('Permission needed', 'Allow saving to your camera roll.');
      return;
    }
    await MediaLibrary.saveToLibraryAsync(uri);
    Alert.alert('Saved', 'Photo saved to your library.');
  };

  if (!apiKeyLoaded) {
    return (
      <View style={styles.center}>
        <ActivityIndicator color="#fff" />
      </View>
    );
  }

  const processing = progress !== null;
  const canProcess = !processing && photos.length > 0 && !!apiKey;

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <View style={styles.header}>
        <View>
          <Text style={styles.title}>Nano Lightroom</Text>
          <Text style={styles.subtitle}>Batch grading via Nano Banana</Text>
        </View>
        <Pressable style={styles.iconButton} onPress={() => setSettingsOpen(true)}>
          <Text style={styles.iconButtonText}>⚙︎</Text>
        </Pressable>
      </View>

      <Text style={styles.sectionLabel}>PRESET</Text>
      <FlatList
        data={PRESETS}
        keyExtractor={(p) => p.id}
        horizontal
        showsHorizontalScrollIndicator={false}
        contentContainerStyle={styles.presetRow}
        renderItem={({ item }) => (
          <PresetCard
            preset={item}
            selected={item.id === selectedPreset.id}
            onPress={() => setSelectedPreset(item)}
          />
        )}
      />

      <Text style={styles.sectionLabel}>PHOTOS</Text>
      <Pressable style={styles.primaryButton} onPress={pickPhotos} disabled={processing}>
        <Text style={styles.primaryButtonText}>
          {photos.length ? `Replace selection (${photos.length})` : 'Pick photos from library'}
        </Text>
      </Pressable>

      {photos.length > 0 && (
        <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.thumbRow}>
          {photos.map((p, i) => (
            <Image key={p.assetId ?? p.uri ?? i} source={{ uri: p.uri }} style={styles.thumb} />
          ))}
        </ScrollView>
      )}

      <Pressable
        style={[styles.processButton, !canProcess && styles.buttonDisabled]}
        onPress={processBatch}
        disabled={!canProcess}
      >
        {processing ? (
          <View style={styles.row}>
            <ActivityIndicator color="#000" />
            <Text style={styles.processButtonText}>
              {`  ${progress.current}/${progress.total}`}
            </Text>
          </View>
        ) : (
          <Text style={styles.processButtonText}>
            {photos.length ? `Process ${photos.length} photo${photos.length === 1 ? '' : 's'}` : 'Process'}
          </Text>
        )}
      </Pressable>

      {results.length > 0 && (
        <>
          <View style={styles.resultsHeader}>
            <Text style={styles.sectionLabel}>RESULTS</Text>
            <Pressable onPress={saveAllToPhotos}>
              <Text style={styles.linkText}>Save all to Photos</Text>
            </Pressable>
          </View>
          {results.map((r) => (
            <ResultCard key={r.id} result={r} onSave={() => r.gradedUri && saveOne(r.gradedUri)} />
          ))}
        </>
      )}

      <SettingsModal
        visible={settingsOpen}
        initialKey={apiKey ?? ''}
        onClose={() => setSettingsOpen(false)}
        onSave={async (k) => {
          await setApiKey(k);
          setApiKeyState(k || null);
          setSettingsOpen(false);
        }}
      />
    </ScrollView>
  );
}

function PresetCard({ preset, selected, onPress }) {
  return (
    <Pressable
      style={[styles.presetCard, selected && styles.presetCardSelected]}
      onPress={onPress}
    >
      <Text style={[styles.presetName, selected && styles.presetNameSelected]} numberOfLines={2}>
        {preset.name}
      </Text>
      <Text style={styles.presetDesc} numberOfLines={3}>
        {preset.description}
      </Text>
    </Pressable>
  );
}

function ResultCard({ result, onSave }) {
  const [showOriginal, setShowOriginal] = useState(false);

  if (result.error) {
    return (
      <View style={[styles.resultCard, styles.resultError]}>
        <Text style={styles.errorText}>Failed: {result.error}</Text>
      </View>
    );
  }

  return (
    <View style={styles.resultCard}>
      <Pressable onPressIn={() => setShowOriginal(true)} onPressOut={() => setShowOriginal(false)}>
        <Image
          source={{ uri: showOriginal ? result.originalUri : result.gradedUri }}
          style={styles.resultImage}
          resizeMode="cover"
        />
        <Text style={styles.resultHint}>
          {showOriginal ? 'ORIGINAL' : 'GRADED — hold to compare'}
        </Text>
      </Pressable>
      <Pressable style={styles.saveButton} onPress={onSave}>
        <Text style={styles.saveButtonText}>Save to Photos</Text>
      </Pressable>
    </View>
  );
}

function SettingsModal({ visible, initialKey, onClose, onSave }) {
  const [draft, setDraft] = useState(initialKey);

  useEffect(() => {
    setDraft(initialKey);
  }, [initialKey, visible]);

  return (
    <Modal visible={visible} animationType="slide" transparent>
      <View style={styles.modalRoot}>
        <View style={styles.modalCard}>
          <Text style={styles.modalTitle}>Gemini API key</Text>
          <Text style={styles.modalHint}>
            Get one at aistudio.google.com/apikey. Stored encrypted on this device only.
          </Text>
          <TextInput
            style={styles.input}
            value={draft}
            onChangeText={setDraft}
            placeholder="AIza…"
            placeholderTextColor="#666"
            autoCapitalize="none"
            autoCorrect={false}
            secureTextEntry
          />
          <View style={styles.modalRow}>
            <Pressable style={styles.modalCancel} onPress={onClose}>
              <Text style={styles.modalCancelText}>Cancel</Text>
            </Pressable>
            <Pressable
              style={[styles.modalSave, !draft && styles.buttonDisabled]}
              disabled={!draft}
              onPress={() => onSave(draft.trim())}
            >
              <Text style={styles.modalSaveText}>Save</Text>
            </Pressable>
          </View>
        </View>
      </View>
    </Modal>
  );
}

function guessMime(fileName, declared) {
  if (declared) return declared;
  const lower = (fileName ?? '').toLowerCase();
  if (lower.endsWith('.png')) return 'image/png';
  if (lower.endsWith('.webp')) return 'image/webp';
  if (lower.endsWith('.heic') || lower.endsWith('.heif')) return 'image/heic';
  return 'image/jpeg';
}

const COLORS = {
  bg: '#0d0d0f',
  card: '#17171a',
  cardSelected: '#fff7d6',
  border: '#26262b',
  text: '#f5f5f7',
  textDim: '#9a9aa2',
  accent: '#ffd84d',
  danger: '#ff5d6c',
};

const styles = StyleSheet.create({
  root: { flex: 1, backgroundColor: COLORS.bg },
  center: { flex: 1, alignItems: 'center', justifyContent: 'center', backgroundColor: COLORS.bg },
  container: { padding: 16, paddingBottom: 80 },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 24,
  },
  title: { color: COLORS.text, fontSize: 28, fontWeight: '700' },
  subtitle: { color: COLORS.textDim, fontSize: 13, marginTop: 2 },
  iconButton: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: COLORS.card,
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1,
    borderColor: COLORS.border,
  },
  iconButtonText: { color: COLORS.text, fontSize: 20 },
  sectionLabel: {
    color: COLORS.textDim,
    fontSize: 11,
    letterSpacing: 1.5,
    fontWeight: '600',
    marginBottom: 8,
    marginTop: 8,
  },
  presetRow: { paddingRight: 16, gap: 10 },
  presetCard: {
    width: 180,
    padding: 14,
    borderRadius: 14,
    backgroundColor: COLORS.card,
    borderWidth: 1,
    borderColor: COLORS.border,
    marginRight: 10,
  },
  presetCardSelected: {
    backgroundColor: COLORS.cardSelected,
    borderColor: COLORS.accent,
  },
  presetName: { color: COLORS.text, fontWeight: '700', fontSize: 14, marginBottom: 4 },
  presetNameSelected: { color: '#1a1a1a' },
  presetDesc: { color: COLORS.textDim, fontSize: 12, lineHeight: 16 },
  primaryButton: {
    backgroundColor: COLORS.card,
    borderRadius: 12,
    paddingVertical: 14,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: COLORS.border,
    marginBottom: 12,
  },
  primaryButtonText: { color: COLORS.text, fontSize: 15, fontWeight: '600' },
  thumbRow: { marginBottom: 12 },
  thumb: { width: 60, height: 60, borderRadius: 8, marginRight: 6 },
  processButton: {
    backgroundColor: COLORS.accent,
    borderRadius: 12,
    paddingVertical: 16,
    alignItems: 'center',
    marginTop: 8,
  },
  processButtonText: { color: '#1a1a1a', fontSize: 16, fontWeight: '700' },
  buttonDisabled: { opacity: 0.4 },
  row: { flexDirection: 'row', alignItems: 'center' },
  resultsHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginTop: 24,
  },
  linkText: { color: COLORS.accent, fontWeight: '600', fontSize: 13 },
  resultCard: {
    backgroundColor: COLORS.card,
    borderRadius: 14,
    overflow: 'hidden',
    marginTop: 12,
    borderWidth: 1,
    borderColor: COLORS.border,
  },
  resultError: { padding: 14 },
  resultImage: { width: '100%', aspectRatio: 1, backgroundColor: '#000' },
  resultHint: {
    color: COLORS.textDim,
    fontSize: 11,
    letterSpacing: 1,
    paddingVertical: 8,
    paddingHorizontal: 12,
  },
  saveButton: { paddingVertical: 12, alignItems: 'center', borderTopWidth: 1, borderTopColor: COLORS.border },
  saveButtonText: { color: COLORS.accent, fontWeight: '600' },
  errorText: { color: COLORS.danger, fontSize: 13 },
  modalRoot: { flex: 1, backgroundColor: 'rgba(0,0,0,0.6)', justifyContent: 'center', padding: 24 },
  modalCard: {
    backgroundColor: COLORS.card,
    borderRadius: 16,
    padding: 20,
    borderWidth: 1,
    borderColor: COLORS.border,
  },
  modalTitle: { color: COLORS.text, fontSize: 18, fontWeight: '700', marginBottom: 4 },
  modalHint: { color: COLORS.textDim, fontSize: 13, marginBottom: 14, lineHeight: 18 },
  input: {
    backgroundColor: '#0a0a0c',
    color: COLORS.text,
    borderRadius: 10,
    padding: 12,
    borderWidth: 1,
    borderColor: COLORS.border,
    fontSize: 14,
    marginBottom: 14,
  },
  modalRow: { flexDirection: 'row', justifyContent: 'flex-end', gap: 10 },
  modalCancel: { paddingVertical: 10, paddingHorizontal: 16 },
  modalCancelText: { color: COLORS.textDim, fontWeight: '600' },
  modalSave: {
    paddingVertical: 10,
    paddingHorizontal: 18,
    borderRadius: 10,
    backgroundColor: COLORS.accent,
  },
  modalSaveText: { color: '#1a1a1a', fontWeight: '700' },
});

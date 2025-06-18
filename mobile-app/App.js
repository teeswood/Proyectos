import React, { useEffect, useState } from 'react';
import { SafeAreaView, View, Text, FlatList, TextInput, Button } from 'react-native';

const API_URL = 'http://localhost:3000';

export default function App() {
  const [materials, setMaterials] = useState([]);
  const [selected, setSelected] = useState(null);
  const [quantity, setQuantity] = useState('');

  useEffect(() => {
    fetch(`${API_URL}/materials`)
      .then(r => r.json())
      .then(setMaterials)
      .catch(console.error);
  }, []);

  const submitRequest = () => {
    if (!selected || !quantity) return;
    fetch(`${API_URL}/requests`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ material_id: selected, quantity: Number(quantity) })
    }).then(() => {
      setQuantity('');
      setSelected(null);
      alert('Solicitud enviada');
    }).catch(console.error);
  };

  return (
    <SafeAreaView style={{ flex: 1, padding: 20 }}>
      <Text style={{ fontSize: 24, marginBottom: 20 }}>Materiales</Text>
      <FlatList
        data={materials}
        keyExtractor={item => String(item.id)}
        renderItem={({ item }) => (
          <View style={{ padding: 10, backgroundColor: selected === item.id ? '#ddd' : '#fff' }}>
            <Text onPress={() => setSelected(item.id)}>{item.name} (stock: {item.stock})</Text>
          </View>
        )}
      />
      <TextInput
        placeholder="Cantidad"
        value={quantity}
        onChangeText={setQuantity}
        keyboardType="numeric"
        style={{ borderWidth: 1, marginTop: 10, padding: 8 }}
      />
      <Button title="Enviar Solicitud" onPress={submitRequest} />
    </SafeAreaView>
  );
}

const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3');
const { open } = require('sqlite');

async function createServer() {
  const app = express();
  app.use(cors());
  app.use(express.json());

  const db = await open({ filename: './warehouse.db', driver: sqlite3.Database });

  await db.exec(`CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0
  );`);

  await db.exec(`CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id INTEGER,
    quantity INTEGER,
    requester TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(material_id) REFERENCES materials(id)
  );`);

  app.get('/materials', async (req, res) => {
    const materials = await db.all('SELECT * FROM materials');
    res.json(materials);
  });

  app.post('/materials', async (req, res) => {
    const { name, stock } = req.body;
    if (!name) return res.status(400).json({ error: 'name required' });
    const result = await db.run('INSERT INTO materials (name, stock) VALUES (?, ?)', name, stock || 0);
    const material = await db.get('SELECT * FROM materials WHERE id = ?', result.lastID);
    res.status(201).json(material);
  });

  app.post('/requests', async (req, res) => {
    const { material_id, quantity, requester } = req.body;
    if (!material_id || !quantity) {
      return res.status(400).json({ error: 'material_id and quantity required' });
    }
    await db.run(
      'INSERT INTO requests (material_id, quantity, requester) VALUES (?, ?, ?)',
      material_id,
      quantity,
      requester || null
    );
    res.status(201).json({ message: 'request saved' });
  });

  app.get('/requests', async (req, res) => {
    const rows = await db.all(
      `SELECT r.id, m.name as material, r.quantity, r.requester, r.created_at
       FROM requests r JOIN materials m ON r.material_id = m.id`
    );
    res.json(rows);
  });

  const port = process.env.PORT || 3000;
  app.listen(port, () => {
    console.log('Server running on port', port);
  });
}

createServer();

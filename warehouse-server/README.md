# Warehouse Server

Simple Express + SQLite backend for managing photovoltaic warehouse materials and field requests.

## Setup

```bash
npm install
npm start
```

The server exposes the following endpoints:

- `GET /materials` – list all materials
- `POST /materials` – add new material `{ name, stock }`
- `GET /requests` – list field requests
- `POST /requests` – create request `{ material_id, quantity, requester }`

Data is stored in `warehouse.db` (SQLite) within the project directory.

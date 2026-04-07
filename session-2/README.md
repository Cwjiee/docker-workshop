# Session 2 – Docker Compose

## Overview

This session introduces **Docker Compose** to run a multi-container application — a **frontend** and a **backend** working together.

```
┌──────────────────────────────────────────────────────┐
│  Your Machine (Host)                                 │
│                                                      │
│   Browser ──► http://localhost:3000  (frontend)      │
│      │                                               │
│      └──────► http://localhost:8000  (backend API)   │
│                                                      │
│  ┌─────────────── Docker Network ──────────────────┐ │
│  │                                                 │ │
│  │  ┌───────────┐          ┌──────────────────┐    │ │
│  │  │ frontend  │          │     backend      │    │ │
│  │  │  (nginx)  │          │    (FastAPI)      │    │ │
│  │  │  :80 ─────┼── 3000   │  :8000 ──────────┼─ 8000
│  │  └───────────┘          └──────────────────┘    │ │
│  └─────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

## How the Two Services Interact

### Backend (`backend` service)

- Built from `./backend` using a Python + FastAPI image.
- Exposes **port 8000** to the host machine.
- Has two API endpoints:
  - `GET /` — Returns a cowsay-formatted "Hello from the Container!" message.
  - `GET /items` — Returns a list of items: `["Docker", "Containers", "Compose"]`.
- Includes CORS middleware so the frontend (running on a different origin/port) can call it.

### Frontend (`frontend` service)

- Built from `./frontend` using an nginx image that serves a static HTML page.
- Exposed on **port 3000** on the host machine.
- The HTML page has two buttons:
  - **Fetch Hello** — calls `http://localhost:8000/` and displays the cowsay output.
  - **Fetch Items** — calls `http://localhost:8000/items` and displays the list.

### Why `localhost:8000`?

The JavaScript runs **in the student's browser** (on the host machine), not inside the container. Since the backend's port 8000 is mapped to the host, the browser can reach it at `http://localhost:8000`.

> **Teaching point:** This is different from container-to-container communication, where services use Docker's internal DNS (e.g., `http://backend:8000`). Browser-based frontends always call from the host's perspective.

## How to Run

1. Copy the example compose file:

   ```bash
   cp compose.yaml.example compose.yaml
   ```

2. Build and start both services:

   ```bash
   docker compose up --build
   ```

3. Open the frontend in your browser:

   ```
   http://localhost:3000
   ```

4. Click the buttons to see the frontend fetch data from the backend!

## File Structure

```
session-2/
├── compose.yaml.example   ← Compose config defining both services
├── README.md              ← This file
├── backend/
│   ├── Dockerfile
│   ├── main.py            ← FastAPI app (/, /items endpoints)
│   └── requirements.txt
└── frontend/
    ├── Dockerfile
    └── index.html          ← Static page with fetch buttons
```

# Demo 2 – Visitor Counter (FastAPI + Redis)

## Overview


This demo introduces using **Docker Compose** to connect a custom web application to a pre-built database container. 

We are building a **Visitor Counter** using a Python FastAPI backend and a **Redis** in-memory database.

```text
┌──────────────────────────────────────────────────────┐
│  Your Machine (Host)                                 │
│                                                      │
│   Browser ──► http://localhost:8000                  │
│                                                      │
│  ┌─────────────── Docker Network ──────────────────┐ │
│  │                                                 │ │
│  │  ┌───────────┐          ┌──────────────────┐    │ │
│  │  │    web    │          │      redis       │    │ │
│  │  │ (FastAPI) │ ◄──────► │ (redis:alpine)   │    │ │
│  │  │  :8000 ───┼── 8000   │      :6379       │    │ │
│  │  └───────────┘          └──────────────────┘    │ │
│  └─────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

## How to Run

Build and start the services:

```bash
    docker compose up --build
```

Open your browser and go to:

```plaintext
    http://localhost:8000
```

Refresh the page a few times and watch the visitor count go up!

When you are done, press CTRL+C in your terminal to stop the containers.

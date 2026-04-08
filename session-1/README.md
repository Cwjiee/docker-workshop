# Session 1 – Docker Basics

## Overview

This session introduces the fundamentals of **Docker** — building images and running containers. It contains two exercises that progressively teach core Docker concepts.

```
┌──────────────────────────────────────────────────────┐
│  Your Machine (Host)                                 │
│                                                      │
│  Exercise 1: dice-roller                             │
│  ┌────────────────────────────────────┐              │
│  │  Container (python:3.13-slim)     │              │
│  │  Interactive CLI dice game        │              │
│  │  (runs with -it flag)             │              │
│  └────────────────────────────────────┘              │
│                                                      │
│  Exercise 2: hello-world                             │
│  ┌────────────────────────────────────┐              │
│  │  Container (python:3.13-slim)     │              │
│  │  FastAPI + cowsay                 │              │
│  │  :8000 ────────────────────────── 8000            │
│  └────────────────────────────────────┘              │
│                                                      │
│   Browser ──► http://localhost:8000                   │
└──────────────────────────────────────────────────────┘
```

---

## Exercise 1: Dice Roller

A simple interactive **Python CLI** app that runs inside a Docker container.

### What It Does

- Prompts the user to enter how many dice to roll.
- Rolls the dice and displays the individual results and the total.
- Keeps running until the user types `q` to quit.

### Key Concepts

- `FROM` — Using a base image (`python:3.13-slim`).
- `WORKDIR` — Setting the working directory inside the container.
- `COPY` — Copying the application source into the image.
- `CMD` — Defining the default command to run.
- Running an **interactive** container with `docker run -it`.

### How to Run

1. Build the image:

   ```bash
   docker build -t dice-roller .
   ```

2. Run the container interactively:

   ```bash
   docker run -it dice-roller
   ```

> **Teaching point:** The `-it` flags attach an interactive terminal so you can type input into the running container. Without them, the container would start and immediately exit since it expects stdin.

---

## Exercise 2: Hello World API

A **FastAPI** web server that returns a cowsay-formatted greeting, demonstrating how to containerise a web application with dependencies.

### What It Does

- Runs a FastAPI server on **port 8000**.
- Has one API endpoint:
  - `GET /` — Returns a cowsay-formatted "Hello from the Container!" message.

### Key Concepts

- `COPY` + `RUN pip install` — Installing Python dependencies from `requirements.txt`.
- `EXPOSE` — Documenting which port the container listens on.
- **Port mapping** with `-p` — Making the container's port accessible on the host.
- Working with a multi-file project (app code + dependencies).

### How to Run

1. Build the image:

   ```bash
   docker build -t hello-world ./backend
   ```

2. Run the container with port mapping:

   ```bash
   docker run -p 8000:8000 hello-world
   ```

3. Open your browser:

   ```
   http://localhost:8000
   ```

> **Teaching point:** The `-p 8000:8000` flag maps the container's internal port 8000 to your machine's port 8000. Without this, the server would be running but unreachable from your browser.

---

## File Structure

```
session-1/
├── README.md              ← This file
├── dice-roller/
│   ├── Dockerfile         ← Simple single-file image
│   └── dice.py            ← Interactive CLI dice game
└── hello-world/
    └── backend/
        ├── Dockerfile         ← Image with pip dependencies
        ├── main.py            ← FastAPI app (/ endpoint)
        └── requirements.txt   ← Python deps (FastAPI, uvicorn, cowsay)
```

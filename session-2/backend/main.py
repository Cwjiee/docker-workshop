from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
import cowsay

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    message = cowsay.get_output_string("cow", "Hello from the Container!")
    return PlainTextResponse(content=message)


@app.get("/items")
def get_items():
    return {"items": ["Docker", "Containers", "Compose"]}

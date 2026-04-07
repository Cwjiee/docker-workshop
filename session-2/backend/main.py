from fastapi import FastAPI
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
    return {"message": message}


@app.get("/items")
def get_items():
    return {"items": ["Docker", "Containers", "Compose"]}

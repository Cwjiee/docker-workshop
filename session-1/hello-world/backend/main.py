from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import cowsay

app = FastAPI()


@app.get("/")
def root():
    message = cowsay.get_output_string("cow", "Hello from the Container!")
    return PlainTextResponse(content=message)

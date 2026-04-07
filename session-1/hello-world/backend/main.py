from fastapi import FastAPI
import cowsay

app = FastAPI()


@app.get("/")
def root():
    message = cowsay.get_output_string("cow", "Hello from the Container!")
    return {"message": message}

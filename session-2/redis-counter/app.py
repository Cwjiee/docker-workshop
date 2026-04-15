from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.get("/")
def read_root():
    count = r.incr('hits')
    return {
        "message": "Hello from Docker Compose!", 
        "total_visits": count
    }

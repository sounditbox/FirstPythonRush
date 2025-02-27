import uvicorn
from fastapi import FastAPI, Response
from prometheus_client import Counter, generate_latest

app = FastAPI()
REQUEST_COUNT = Counter("request_count", "Total number of page visits")


@app.get("/")
def root():
    REQUEST_COUNT.inc()
    return {
        "message": f"This page was visited {REQUEST_COUNT._value.get()} times"}


@app.get("/metrics")
def metrics():
    content = generate_latest()
    return Response(content=content, media_type="text/plain")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

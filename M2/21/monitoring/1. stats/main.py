import uvicorn
from fastapi import FastAPI


class Counter:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1

    def __int__(self):
        return self.count

    def __str__(self):
        return str(self.count)


counter = Counter()
app = FastAPI()


@app.get("/")
def root():
    counter.inc()
    return {"message": f"This page was visited {counter} times"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

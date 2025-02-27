from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    with open("data/data.txt", "r") as f:
        data = f.read()
        count = int(data if data else "0") + 1
    with open("data/data.txt", "w") as f:
        f.write(str(count))
    return {"count": count}

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"messages": ["Hello World!!!", "Goodbye World!!!"]}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/divide")
async def divide(a: float, b: float):
    return {"result": a / b}

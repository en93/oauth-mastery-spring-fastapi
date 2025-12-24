from fastapi import FastAPI

app = FastAPI()

@app.post("/hello")
async def root():
    return {"message": "Hello World"}
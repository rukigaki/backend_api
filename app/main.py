import uvicorn
from fastapi import FastAPI
from api_v1.handlers import router as user_router


app = FastAPI()
app.include_router(user_router)

@app.get("/")
async def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)

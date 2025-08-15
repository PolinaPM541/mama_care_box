from fastapi import FastAPI

from app.router import router

app = FastAPI(title="Mama Care Box")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9000)

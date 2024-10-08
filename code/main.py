from fastapi import FastAPI
from api import router as api_router
from database import engine, database
from models import metadata

app = FastAPI()

app.include_router(api_router)

metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

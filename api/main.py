from fastapi import FastAPI
from api.utils.dbUtils import database
from api.auth import router as auth_router
app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="Api{TestFastApi}",
    description="Testing python fastapi",
    version=0.10,
    openapi_url="/openapi.json"
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(auth_router.router, tags=["Auth"])

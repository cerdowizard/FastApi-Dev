from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import uvicorn
import models
from adminActions.adminRouters import adminRoute
from post.post_router import post_router
from user.router import user_router
from utils.database import database, engine
from auth import router as auth_router

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="Api{Blog It}",
    description="Testing python fastapi",
    version=0.10,
    openapi_url="/openapi.json"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


def create_tables():  # new
    models.Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup():
    await database.connect()
    create_tables()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


app.include_router(auth_router.router, tags=["Auth"])
app.include_router(adminRoute, tags=["Admin Action"])
app.include_router(user_router, tags=["User"])
app.include_router(post_router, tags=["Post"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="1530")

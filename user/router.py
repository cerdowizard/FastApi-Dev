from fastapi import APIRouter

user_router = APIRouter(
    prefix="/api/v1/auth"
)


@user_router.get("/get/user{id}")
async def get_user():
    pass


@user_router.put("/update/user/{id}")
async def update_user_profile():
    pass


@user_router.delete("/delete/user/{id}")
async def delete_user_profile_delete():
    pass


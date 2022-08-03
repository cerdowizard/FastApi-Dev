import fastapi
import re
from fastapi import Depends, HTTPException
from api.auth import schema, crud
from api.utils import cryptoUtil
from fastapi.security import OAuth2PasswordRequestForm

router = fastapi.APIRouter(
    prefix="/api/v1/auth"
)


@router.post("/register", response_model=schema.ListUser)
async def register(user: schema.UserCreate):
    # check user exist
    result = await crud.find_exist_user(user.email)
    if result:
        raise HTTPException(status_code=404, detail="User already exist")
    # if len(user.password) < 6:
    #     raise HTTPException(status_code=400, detail="password must not be less than six characters")

    if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', user.password):
        raise HTTPException(status_code=400, detail="password must not be less than 8 characters and must contain one "
                                                    "capital letter, small letter and a symbol ")
    if user.password != user.cn_password:
        raise HTTPException(status_code=400, detail="password and confirm password must be the same")
    # create User
    user.password = cryptoUtil.hash_password(user.password)
    await crud.save_new_user(user)
    return {**user.dict()}


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # check if user exist
    result = await crud.find_exist_user(form_data.username)
    if not result:
        raise HTTPException(status_code=404, detail="User do not exist in database")

    # check password

    user = schema.UserPassword(**result)
    verify_password = cryptoUtil.verify_password(form_data.password, user.password)

    if not verify_password:
        raise HTTPException(status_code=422, detail="Incorrect Password")
    return form_data

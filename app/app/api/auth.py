import json
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from tortoise.exceptions import IntegrityError
from models.user import User
from utils.security import verify_password, get_password_hash
from utils.token import create_access_token, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES
from schemas.user import PasswordChangeRequest, UserCreate, UserResponse,UserLogin

auth_router = APIRouter()


@auth_router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    print('register')
    try:
        user_obj = await User.create(
            username=user.username,
            email=user.email,
            password=get_password_hash(user.password),
        )
        return UserResponse.model_validate(user_obj)
    except IntegrityError as e:
        if "username" in str(e):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A user with this username already exists."
            )
        elif "email" in str(e):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A user with this email already exists."
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="An unknown error occurred."
            )


@auth_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print(f"Received username: {form_data.username}, password: {form_data.password}")
    user = await User.get(username=form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.get("/users/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@auth_router.put("/password", response_model=UserResponse)
async def change_password(
    password_change_request: PasswordChangeRequest,
    current_user: User = Depends(get_current_user)
):
    print('修改密码')
    if not verify_password(password_change_request.old_password, current_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Old password is incorrect."
        )

    current_user.password = get_password_hash(password_change_request.new_password)
    await current_user.save()
    return UserResponse.model_validate(current_user)
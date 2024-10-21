from fastapi import APIRouter, Depends, HTTPException, status
from .auth import get_current_user
from app.models.user import User

admin_router = APIRouter()

async def get_admin_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to access this resource",
        )
    return current_user

@admin_router.get("/admin-dashboard")
async def admin_dashboard(admin_user: User = Depends(get_admin_user)):
    return {"message": "Welcome to the admin dashboard", "username": admin_user.username}

@admin_router.get("/users")
async def list_users(admin_user: User = Depends(get_admin_user)):
    users = await User.all()
    return users

from fastapi import APIRouter
from app.api import admin,auth

# 创建一个全局的 APIRouter 实例
api_router = APIRouter()

# 包含不同模块的路由
api_router.include_router(auth.auth_router, prefix="/users", tags=["Users"])
api_router.include_router(admin.admin_router, prefix="/admin", tags=["Admin"])
# api_router.include_router(company.router, prefix="/companies", tags=["Companies"])
# api_router.include_router(risk.router, prefix="/risks", tags=["Risks"])

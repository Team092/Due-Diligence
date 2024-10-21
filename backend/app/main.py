from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import api_router
from app.db.init_db import init_db
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 在应用启动前初始化数据库
    await init_db(app)
    yield
    # 在应用关闭时执行清理工作（如果需要）

app = FastAPI(lifespan=lifespan)

# 配置 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源进行跨域请求，建议在生产环境中替换为特定的前端 URL
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)

# 包含全局 API 路由
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Research Due Diligence System"}

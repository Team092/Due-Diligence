from fastapi import FastAPI
from contextlib import asynccontextmanager
from api import api_router
from db.init_db import init_db
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 在应用启动前初始化数据库
    await init_db(app)
    yield
    # 在应用关闭时执行清理工作（如果需要）

app = FastAPI(lifespan=lifespan)

origins = [
    "http://127.0.0.1:8848",
    # 添加你允许的前端应用的源地址
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 包含全局 API 路由
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Research Due Diligence System"}



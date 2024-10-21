from pydantic import BaseModel, EmailStr, constr

# 用户注册请求模型
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# 用户登录请求模型
class UserLogin(BaseModel):
    username: str
    password: str

# 响应用户数据模型
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    # password:str

    model_config = {
        "from_attributes": True  # 使用 model_config 代替 Config 进行配置
    }

class PasswordChangeRequest(BaseModel):
    old_password: str
    new_password: str
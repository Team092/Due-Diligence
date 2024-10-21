FROM python:3.12-slim

# 设置工作目录
WORKDIR /code

# 仅复制 requirements.txt 文件并安装依赖
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# CMD 由 docker-compose.yml 中的 command 覆盖，保持不变
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

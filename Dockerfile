# 使用官方 Python 基础镜像
FROM python:3.8

ENV http_proxy "http://127.0.0.1:7890"
ENV https_proxy "http://127.0.0.1:7890"

# 设置工作目录为 /JY_monitor_docker_app
WORKDIR /JY_monitor_docker_app

# 将当前目录内容复制到容器内的 /JY_monitor_docker_app
COPY . /JY_monitor_docker_app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置环境变量
ENV PYTHONUNBUFFERED 1

# 运行时容器监听的端口号（如果需要的话）
# EXPOSE 8000

# 定义容器启动时执行的命令
CMD ["python3", "main.py"]

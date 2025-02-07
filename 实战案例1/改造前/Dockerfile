# 基于 Ubuntu 镜像
FROM arm64v8/ubuntu:20.04

# 设置环境变量，避免安装过程中出现交互提示
ENV DEBIAN_FRONTEND=noninteractive

# 安装必要的系统依赖和工具
RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    ca-certificates \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 下载并安装 Miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

# 将 Miniconda 添加到系统路径
ENV PATH /opt/conda/bin:$PATH

# 创建名为 rag1 的 Conda 环境
RUN conda create -n rag1 python=3.9

# 激活 rag1 环境
RUN echo "source activate rag1" > ~/.bashrc
ENV PATH /opt/conda/envs/rag1/bin:$PATH

# 设置工作目录
WORKDIR /app

# 将本地代码复制到容器的工作目录
COPY . .

# 在 rag1 环境中使用 pip 安装项目依赖
RUN pip install -r requirements.txt

# 运行 Django 数据库迁移命令
RUN python manage.py migrate

# 暴露 Django 开发服务器默认端口
EXPOSE 8000

# 启动 Django 开发服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
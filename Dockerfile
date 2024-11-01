# Pythonの公式イメージを使用
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# requirements.txtをコンテナにコピー
COPY requirements.txt .

# ライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt



# gitをインストールする
# パッケージリストを更新し、gitをインストール
RUN apt-get update && apt-get install -y git

# Gitの設定
RUN git config --global user.name "KENTAROSZK" \
    && git config --global user.email "szkkntru2@gmail.com"
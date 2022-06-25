FROM python:3.6
ENV PYTHONUNBUFFERED 1
#/codeディレクトリ作成
RUN mkdir /code
# 各種命令実行のカレントディレクトリを指定
WORKDIR /code
# ローカルのrequirements.txtをコンテナ内の/code/にコピー
ADD requirements.txt /code/
# コマンド実行
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/
FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
ENV WORKDIR /opt/app
WORKDIR ${WORKDIR}
COPY requirements.txt ${WORKDIR}
RUN mkdir -p /var/log/uwsgi/ && touch uwsgi.log
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apt update
RUN apt install -y vim
COPY . ${WORKDIR}
#コンテナ作成時に実行されるコマンド
CMD ["uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini"]
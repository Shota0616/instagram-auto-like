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
RUN apt install unzip
RUN apt install wget
# chromedriver
# RUN wget https://chromedriver.storage.googleapis.com/110.0.5481.30/chromedriver_linux64.zip
# RUN unzip /opt/app/chromedriver_linux64.zip
RUN cp chromedriver /usr/local/bin/
RUN chmod 755 /usr/local/bin/chromedriver
# chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
# RUN apt install -y rabbitmq-server=3.8.9-3
# RUN rabbitmq-plugins enable rabbitmq_management
# RUN rabbitmqctl add_user admin admin
# RUN rabbitmqctl set_user_tags admin administrator
# RUN rabbitmqctl set_permissions admin '.*' '.*' '.*'
# RUN apt install -y redis-server=5:6.0.16-1+deb11u2
COPY . ${WORKDIR}
#コンテナ作成時に実行されるコマンド
CMD ["uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini"]
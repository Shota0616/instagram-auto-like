FROM ubuntu:22.10
ENV PYTHONUNBUFFERED 1
ENV WORKDIR /opt/app
WORKDIR ${WORKDIR}
COPY requirements.txt ${WORKDIR}
RUN mkdir -p /var/log/uwsgi/ && touch uwsgi.log
# python install
RUN apt install -y build-essential libbz2-dev libdb-dev \
libreadline-dev libffi-dev libgdbm-dev liblzma-dev \
libncursesw5-dev libsqlite3-dev libssl-dev \
zlib1g-dev uuid-dev tk-dev wget
RUN wget https://www.python.org/ftp/python/3.9.16/Python-3.9.16.tar.xz
WORKDIR /Python-3.9.16
RUN ./configure
RUN make
RUN make install


RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apt update
RUN apt install -y vim x11vnc xvfb fluxbox wget wmctrl gnupg2 unzip
# chromedriver
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt -y install google-chrome-stable
# RUN wget https://chromedriver.storage.googleapis.com/110.0.5481.30/chromedriver_linux64.zip
# RUN unzip /opt/app/chromedriver_linux64.zip
# COPY chromedriver /usr/local/bin/
# RUN chmod 755 /usr/local/bin/chromedriver
# COPY ./google-chrome-stable_current_amd64.deb /usr/local/src/
# RUN apt install -y /usr/local/src/google-chrome-stable_current_amd64.deb
# RUN apt install -y xserver-xorg
# RUN apt -y install x11-apps
# chrome
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN apt install -y rabbitmq-server=3.8.9-3
# RUN rabbitmq-plugins enable rabbitmq_management
# RUN rabbitmqctl add_user admin admin
# RUN rabbitmqctl set_user_tags admin administrator
# RUN rabbitmqctl set_permissions admin '.*' '.*' '.*'
# RUN apt install -y redis-server=5:6.0.16-1+deb11u2
COPY . ${WORKDIR}
#コンテナ作成時に実行されるコマンド
CMD uwsgi --ini /etc/uwsgi/uwsgi.ini
CMD /etc/init.d/dbus start
# CMD google-chrome --no-sandbox
FROM ubuntu:22.10
ENV PYTHONUNBUFFERED 1
ENV WORKDIR /opt/app
ENV TZ=Asia/Tokyo
WORKDIR ${WORKDIR}
COPY requirements.txt ${WORKDIR}
RUN mkdir -p /var/log/uwsgi/ && touch uwsgi.log
# python install
RUN apt update && apt install tzdata && apt install -y --no-install-recommends wget build-essential libreadline-dev \
libncursesw5-dev libssl-dev libsqlite3-dev libgdbm-dev libbz2-dev liblzma-dev zlib1g-dev uuid-dev libffi-dev libdb-dev \
tzdata wget vim unzip

#任意バージョンのpython install
RUN wget --no-check-certificate https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz \
&& tar -xf Python-3.9.5.tgz \
&& cd Python-3.9.5 \
&& ./configure --enable-optimizations\
&& make \
&& make install
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade wheel
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

# chromedriver
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
# RUN apt -y install google-chrome-stable
COPY . ${WORKDIR}
#コンテナ作成時に実行されるコマンド
CMD uwsgi --ini /etc/uwsgi/uwsgi.ini
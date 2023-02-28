FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
ENV WORKDIR /opt/app
ENV TZ=Asia/Tokyo
WORKDIR ${WORKDIR}
COPY requirements.txt ${WORKDIR}
COPY . ${WORKDIR}
RUN mkdir -p /var/log/uwsgi/ && touch uwsgi.log
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apt update && apt install -y vim wget unzip curl gnupg

# chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*

# chrome driver
ADD https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_linux64.zip /opt/chrome/
RUN cd /opt/chrome/ && \
    unzip chromedriver_linux64.zip && \
    rm -f chromedriver_linux64.zip


#コンテナ作成時に実行されるコマンド
CMD /usr/local/bin/uwsgi --ini /etc/uwsgi/uwsgi.ini
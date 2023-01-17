FROM nginx:1.23.1
ENV SSL_WORKDIR /etc/ssl
#buildのとき実行されるコマンド
RUN apt update
RUN apt install -y vim
WORKDIR ${SSL_WORKDIR}
RUN apt install openssl
FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
ENV WORKDIR /opt/app
WORKDIR ${WORKDIR}
COPY requirements.txt ${WORKDIR}
COPY ./conf/uwsgi.ini /etc/uwsgi/
RUN mkdir -p /var/log/uwsgi/ && touch uwsgi.log
RUN mkdir -p /var/run/uwsgi/ && touch uwsgi.sock
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apt update
RUN apt install -y vim
COPY . ${WORKDIR}
CMD ["uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini"]
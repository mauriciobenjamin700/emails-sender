FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y postfix && \
    apt-get clean

COPY postfix/main.cf /etc/postfix/main.cf

CMD ["postfix", "start-fg"]
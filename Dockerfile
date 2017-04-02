FROM fedora:latest

RUN dnf update -y && dnf clean all
RUN dnf install -y python3-bottle && dnf clean all
ENV LANG en_US.UTF-8

EXPOSE 80
WORKDIR /root/www

ADD fmfi /root/www

# external url and port
RUN sed -i 's|base_url = .*$|base_url = "http://localhost:8080/"|' /root/www/config.py

CMD python3 fmfimain.py

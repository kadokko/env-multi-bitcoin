FROM python:3.7

RUN pip install flask flask-cors requests

RUN groupadd cors \
&&  useradd -g cors -s /bin/bash -m cors

USER cors
WORKDIR /home/cors

ADD cors.py /home/cors/.

EXPOSE 5000

CMD ["tail", "-f", "/dev/null"]

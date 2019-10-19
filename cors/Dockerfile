FROM python:3.8.0-alpine3.10

RUN pip install flask flask-cors requests

RUN addgroup -S cors \
&&  adduser -S cors -G cors

USER cors
WORKDIR /home/cors

COPY cors.py /home/cors/.

EXPOSE 5000

CMD ["tail", "-f", "/dev/null"]

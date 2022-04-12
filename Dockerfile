FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app
ENTRYPOINT [ "python" ]
CMD ["/app/wsgi.py"]
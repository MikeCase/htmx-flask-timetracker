FROM python:3.8-buster

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app
ENTRYPOINT [ "gunicorn" ]
CMD ["-b", "0.0.0.0:5555", "wsgi:time_tracker"]
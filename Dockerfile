FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

CMD ["gunicorn", "-b", "0.0.0.0:5555", "wsgi:app"]
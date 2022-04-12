FROM python:3.8-buster

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

CMD ["gunicorn", "-b", "0.0.0.0:5555", "time_tracker:app"]
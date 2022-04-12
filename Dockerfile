FROM python:3.8-buster

WORKDIR /

COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

COPY . /

CMD ["gunicorn", "-b", "0.0.0.0:5555", "time_tracker:app"]
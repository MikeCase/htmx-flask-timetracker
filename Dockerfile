FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "0.0.0.0:5555", "time_tracker:app"]
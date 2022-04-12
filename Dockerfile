FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python3.8 -m venv .venv
RUN source .venv/bin/activate
RUN pip install -r requirements.txt

COPY . /app

CMD ["gunicorn", "-b", "0.0.0.0:5555", "time_tracker:app"]
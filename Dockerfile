FROM python:3.8-alpine

WORKDIR /time_app

COPY requirements.txt /time_app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /time_app

CMD ["gunicorn", "-b", "0.0.0.0:5555", "time_tracker:app"]
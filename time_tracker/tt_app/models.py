from datetime import datetime 
from time_tracker import db

class TimeClock(db.Model):
    dt_id = db.Column(db.Integer, primary_key=True)
    dt_in = db.Column(db.Text)
    dt_out = db.Column(db.Text)
    clock_total = db.Column(db.Text)

    def __init__(self, dt_in, dt_out=None, clock_total=0):
        self.dt_in = dt_in
        self.dt_out = dt_out
        self.clock_total = clock_total


    
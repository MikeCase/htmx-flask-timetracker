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


    def to_dt(self):
        in_time = datetime.strptime(self.dt_in, "%Y-%m-%d %H:%M:%S.%f")
        if self.dt_out: 
            if self.dt_out is str():
                out_time = datetime.strptime(self.dt_out, "%Y-%m-%d %H:%M:%S.%f")
            elif self.dt_out is datetime:
                out_time = self.dt_out
                return in_time, out_time
        else:
            return

    def td_to_hms(self, td):
        t_seconds = td.total_seconds()
        hours = t_seconds // 3600
        minutes = (t_seconds % 3600) // 60
        seconds = t_seconds % 60
        return hours, minutes, seconds
    
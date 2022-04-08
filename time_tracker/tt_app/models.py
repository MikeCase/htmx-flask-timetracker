from datetime import datetime 
from time_tracker import db

class TimeClock(db.Model):
    dt_id = db.Column(db.Integer, primary_key=True)
    dt_date = db.Column(db.Date)
    dt_in = db.Column(db.DateTime)
    dt_out = db.Column(db.DateTime)
    clock_total = db.Column(db.Text)

    def __init__(self, dt_in, dt_out=None, clock_total=0):
        self.dt_date = datetime.today()
        self.dt_in = dt_in
        self.dt_out = dt_out
        self.clock_total = clock_total

    def total_clock_time(self):
        in_time = self.dt_in
        out_time = self.dt_out
        return out_time - in_time

    def td_to_hms(self, td):
        t_seconds = td.total_seconds()
        hours = t_seconds // 3600
        minutes = (t_seconds % 3600) // 60
        seconds = t_seconds % 60
        return hours, minutes, seconds


    def process_total_time(self, clock_date):
        pass
    
    # def get_date_range(self, start_date, end_date):
    #     date_range = self.query.filter(and_(self.dt_in >= start_date, self.dt_in <= end_date))
    #     print(date_range)

class TCReports():

    def __init__(self, start_date, end_date):
        self.tc_start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.tc_end_date = datetime.strptime(end_date, "%Y-%m-%d")
        

    def build_report(self):
        pass
    
    
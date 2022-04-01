from time_tracker import app, db
from flask import render_template, redirect
from sqlalchemy import desc
from time_tracker.tt_app.models import TimeClock
from datetime import datetime

@app.route('/')
def index():
    return render_template('./index.html')

@app.post('/clock_out/<dt_id>')
def clock_out(dt_id):
    current_time = datetime.now()
    t_clock = TimeClock.query.get(dt_id)
    t_clock.dt_out = current_time
    stime = datetime.strptime(t_clock.dt_in, "%Y-%m-%d %H:%M:%S.%f")
    etime = t_clock.dt_out
    total_time = etime - stime
    t_clock.clock_total = f"{total_time.seconds}"
    db.session.commit()
    
    return render_template('./index.html')


@app.post('/clock_in')
def clock_in():
    current_time = datetime.now()
    t_clock = TimeClock(dt_in=current_time)
    db.session.add(t_clock)
    db.session.commit()
    clocks = []
    clock_times = TimeClock.query.order_by(desc(TimeClock.dt_id)).all()
    for clock in clock_times:
        
        dt_in = datetime.strptime(clock.dt_in, "%Y-%m-%d %H:%M:%S.%f")
        dt_total = clock.clock_total
        clock_id = clock.dt_id
        if clock.dt_out != None:
            dt_out = datetime.strptime(clock.dt_out, "%Y-%m-%d %H:%M:%S.%f")
        else:
            dt_out = None
            
        clocks.append([clock_id, dt_in, dt_out, dt_total])

    return render_template('./clockin.html', clock_time=clocks)

@app.get('/clocks')
def clocks():
    clocks = []
    clock_times = TimeClock.query.order_by(desc(TimeClock.dt_id)).all()
    
    for clock in clock_times:
        dt_in = datetime.strptime(clock.dt_in, "%Y-%m-%d %H:%M:%S.%f")
        dt_total = clock.clock_total
        clock_id = clock.dt_id
        if clock.dt_out != None:
            dt_out = datetime.strptime(clock.dt_out, "%Y-%m-%d %H:%M:%S.%f")
        else:
            dt_out = None

        clocks.append([clock_id, dt_in, dt_out, dt_total])
    return render_template('./clockin.html', clock_time=clocks)

def create_db():
    pass
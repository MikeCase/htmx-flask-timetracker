import os
from time_tracker import app, db
from time_tracker.models import TimeClock, TCReports
from time_tracker.helpers import total_time, list_clocks, create_xl
from flask import render_template, redirect, send_from_directory
from sqlalchemy import desc, func, distinct
from datetime import datetime, date



@app.route('/')
def index():
    
    return render_template('./index.html')


@app.post('/clock_out/<dt_id>')
def clock_out(dt_id):
    current_time = datetime.now()
    t_clock = TimeClock.query.get(dt_id)
    t_clock.dt_out = current_time
    total_time = t_clock.total_clock_time()
    hours, minutes, seconds = t_clock.td_to_hms(total_time)
    t_clock.clock_total = f"{round(hours)},{round(minutes)},{round(seconds)}"
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
    
    clocks = list_clocks(clock_times)
    
    return render_template('./clockin.html', clock_time=clocks)


@app.get('/clocks')
def clocks():
    clocks = []
    clock_times = TimeClock.query.order_by(desc(TimeClock.dt_id)).all()
    
    clocks = list_clocks(clock_times)

    return render_template('./clockin.html', clock_time=clocks)

## Route for showing the report page
@app.get('/reports/<report_date>')
def get_report_date(report_date):
    """Reports page view"""

    # these two lines are another way to create the date.
    # datelist=report_date.split('-')  
    # report_date = date(year=int(datelist[0]),month=int(datelist[1]), day=int(datelist[2])) 

    # How to query by date. 
    report_date = datetime.strptime(f"{report_date} 00:00:00.00", "%Y-%m-%d %H:%M:%S.%f")
    report_for_date = TimeClock.query.filter(func.date(TimeClock.dt_in) == func.date(report_date)).all()
    
    # Get the total for clock time
    total_times = total_time(report_for_date)
    return render_template('./reports.html', totals_for_date=total_times, report_date=report_date, report_for_date=report_for_date)

## Route for building a report
@app.get('/reports')
def get_dates_list():
    # get a list of distinct dates for reports
    dist_dates = db.session.query(TimeClock.dt_date.distinct().label("dt_date")).all()
    dates = []
    for d in dist_dates:
        for dd in d:
            dates.append(dd)
    
    return render_template('./reports_list.html', report_dates=dates)

## Route to show/save a report
@app.get('/reports/save/<report_date>')
def save_report(report_date):
    report_date = datetime.strptime(f"{report_date} 00:00:00.00", "%Y-%m-%d %H:%M:%S.%f")
    report_for_date = TimeClock.query.filter(func.date(TimeClock.dt_in) == func.date(report_date)).all()
    print('Sending to create_xl()')
    filename = create_xl(report_date, report_list=report_for_date)
    print(filename)
    reports_folder = os.path.join(app.root_path, app.config['UPLOADS_FOLDER'])
    totals = total_time(report_for_date)
    # return render_template("./reports.html", report_for_date=report_for_date, totals_for_date=totals)

    try:
        return send_from_directory(reports_folder, path=filename, as_attachment=True)
    except FileNotFoundError:
        print(app.config['UPLOADS_FOLDER'])
        abort(404)
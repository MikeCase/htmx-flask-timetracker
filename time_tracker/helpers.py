import os
from time_tracker import app
from openpyxl import Workbook
# from openpyxl import get_column_letter
from datetime import datetime

def create_xl( report_date, report_list=None):
    wb = Workbook()
    dest_filename = os.path.join(app.root_path, f"{app.config['UPLOADS_FOLDER']}/{report_date.strftime('%Y_%M_%d')}.xlsx")
    print(dest_filename)
    ws = wb.active
    
    if report_list != None:
        for data in report_list:
            if data.dt_out != None:
                h,m,s = data.clock_total.split(",")
                
                ws.append([data.dt_in.strftime("%I:%M:%S"), data.dt_out.strftime("%I:%M:%S"), h, m, s])
    
    wb.save(dest_filename)
    return f"{report_date.strftime('%Y_%M_%d')}.xlsx"

def list_clocks(clock_times):
    clocks = []
    for clock in clock_times:
            
            dt_in = clock.dt_in
            if clock.clock_total != None:
                dt_total = clock.clock_total
            else:
                dt_toal = None
            clock_id = clock.dt_id
            if clock.dt_out != None:
                dt_out = clock.dt_out
            else:
                dt_out = None
                
            clocks.append([clock_id, dt_in, dt_out, dt_total])

    return clocks

def total_time(report_day):
    """Total the clock times from a specified date."""
    ht = 0
    mt = 0
    st = 0

    for clock_time in report_day:
        # Split the clock_time into hours(h), minutes(m) and seconds(s)
        if clock_time.dt_out != None and clock_time.clock_total != None:
            # print(clock_time.clock_total)
            h,m,s = clock_time.clock_total.split(',')
            # Convert to integers
            h = int(h)
            m = int(m)
            s = int(s)
            
            # Start adding the hours, minutes and seconds together and adding them to the 
            # totals(ht, mt, st)
            ht = ht + h
            mt = mt + m 

            # If the minutes total(mt) >= 60 (1 hour) 
            # subtract 60 from minutes total(mt) and add 1 to hour total(ht)
            if mt >= 60:
                mt = mt - 60 
                ht = ht + 1
            
            # Same same for seconds. 
            st = st + s
            if st >= 60:
                st = st - 60
                mt = mt + 1
        else:
            ht = ht
            mt = mt
            st = st

        # print(f"{ht}h {mt}m {st}s")
        total_times = [ht, mt, st] # Add the totals to a list and ship off to the view. 
    return total_times


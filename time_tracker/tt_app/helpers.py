def total_time(report_day):
    """Total the clock times from a specified date."""
    ht = 0
    mt = 0
    st = 0

    for clock_time in report_day:
        # Split the clock_time into hours(h), minutes(m) and seconds(s)
        if clock_time.clock_total != None:
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


        # print(f"{ht}h {mt}m {st}s")
        total_times = [ht, mt, st] # Add the totals to a list and ship off to the view. 
    return total_times


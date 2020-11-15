import datetime

day = datetime.datetime(2017,1,1)

sunday_list = []

while day < datetime.datetime(2020,1,27):

    if day.weekday() == 6:
        sunday_list.append(day)
    
    day += datetime.timedelta(days=1)


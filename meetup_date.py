import datetime
import calendar
import pprint

from enum import IntEnum

class Weekday(IntEnum):
        SUNDAY = 6
        MONDAY = 0
        TUESDAY = 1
        WEDNESDAY = 2
        THURSDAY = 3
        FRIDAY = 4
        SATURDAY = 5

def meetup_date(year, month, nth=4, weekday=3):
    '''
    Calculate date of 4th Thursday of the month
    '''
    month_calendar = calendar.monthcalendar(year, month)
    certain_week_days = [ week[weekday] for week in month_calendar]

    try:
        if nth > 0:
            day = certain_week_days[nth-1] if certain_week_days[0] else certain_week_days[nth]
        else:
            day = certain_week_days[nth] if certain_week_days[-1] else certain_week_days[nth-1]
    except IndexError:
        return 'No such data'


    return datetime.date(year, month, day)




def main():
    print(meetup_date(2012,3))
    print(meetup_date(2010, 6, nth=-1, weekday=Weekday.FRIDAY))


if __name__ == '__main__':
    main()


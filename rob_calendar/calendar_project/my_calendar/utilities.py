# from datetime import datetime,timedelta
from calendar import HTMLCalendar

from .models import Appointment

class MyCalendar(HTMLCalendar):
    def __init__(self,year=None,month=None):
        self.year = year
        self.month = month
        super(MyCalendar, self).__init__()

    def formatDay(self,day,appointments):
        days_appointments = appointments.filter(start_time_day=day)
        d = ''
        for appt in days_appointments:
            d += f'<li class="calendar_list">{appt.get_html_url}</li>'
        if day != 0:
            return f'<td><span class="date">{day}</span><ul>{d}</ul></td>'
        return '<td></td>'

    def formatWeek(self,theweek):
        week = ''
        for day,weekday in theweek:
            week += self.formatday(day)
        return f"<tr> {week} </tr>"

    def formatMonth(self,with_year=True):
        appointments = Appointment.objects.filter(start_time_year=self.year,start_time_month=self.month)
        cal = f'<table border="3" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year,self.month,withyear=with_year)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += self.formatWeek(week)
        return cal
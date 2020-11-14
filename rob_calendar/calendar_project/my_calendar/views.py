from django.shortcuts import render
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

import calendar
from datetime import datetime,date,timedelta

from .utilities import MyCalendar
from .models import Appointment
# Create your views here.


def get_date(date_data):
    if date_data:
        year, month = (int(x) for x in date_data.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def previous_month(date_data):
    prev_month = date_data.replace(day=1) - timedelta(days=1)
    return str(prev_month.year) + '-' + str(prev_month.month)


def next_month(date_data):
    nm = date_data.replace(day=calendar.monthrange(date_data.year,
                                                   date_data.month)[-1]) + timedelta(days=1)
    return str(nm.year) + '-' + str(nm.month)


def home(request):
    return render(request,'my_calendar/home.html')


def about(request):
    return render(request,'my_calendar/about.html')


class CalendarView(ListView):
    model = Appointment
    template_name = "my_calendar/calendar.html"
    success_url = reverse_lazy("calendar")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month',None))
        cal = MyCalendar(d.year,d.month)
        html_calendar = cal.formatMonth(with_year=True)
        context['calendar'] = mark_safe(html_calendar)
        context['prev_month'] = previous_month(d)
        context['next_month'] = next_month(d)
        return context

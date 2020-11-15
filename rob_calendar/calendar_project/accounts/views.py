from django.shortcuts import render
from django.urls import path,include
from . import models
from . import api


# ViewSets define the view behavior.


def accounts(request):
    return render(request,'my_calendar/home.html')
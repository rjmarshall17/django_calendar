from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='Calendar-Home'),
    path('about/',views.about,name='about-calendar'),
]
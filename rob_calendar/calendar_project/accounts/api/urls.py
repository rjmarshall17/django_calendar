from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('account_details/',views.api_detail_account_view,name='detail'),
]

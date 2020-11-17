from django.urls import path, include
# from rest_framework import routers
from .api import views

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'accounts', views.AccountViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', views.login_account,name='login'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from django.shortcuts import render
from django.urls import path,include
from rest_framework import permissions, viewsets
from . import api.serializers
from . import models


# ViewSets define the view behavior.


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Account.objects.all().order_by('-date_created')
    serializer_class = serializers.AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


def accounts(request):
    return render(request,'my_calendar/home.html')
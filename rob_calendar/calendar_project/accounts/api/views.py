from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import permissions, viewsets

from ..models import Account
from ..forms import AccountForm
from . import serializers


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all().order_by('-date_created')
    serializer_class = serializers.AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET', ])
def api_detail_account_view(request):
    try:
        account_detail = Account.objects.get()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.AccountSerializer(account_detail)
    return Response(serializer.data)


@api_view(['PUT', ])
def api_update_account_view(request):
    try:
        account_data = Account.objects.get()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.AccountSerializer(account_data, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['success'] = "Account updated"
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_account_view(request):
    try:
        account_data = Account.objects.get()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    operation = account_data.delete()
    data = {}
    if operation:
        data['success'] = 'Delete succeeded'
    else:
        data['failure'] = 'Delete failed'
    return Response(data=data)


@api_view(['POST', ])
@permission_classes([AllowAny])
def registration(request):
    if request.method == 'POST':
        print(request.POST)
        form = AccountForm(request.POST)
        render(request, 'accounts/registration.html', {'form': form})
        print("\n******** RJM: form.errors=>%s<" % form.errors)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            print("***** RJM: The form is valid, the first name is: %s" % first_name)
            form.save()
        else:
            print("\n***** RJM: The form is NOT valid\n")
    return render(request, 'accounts/registration.html', {'form': form})

    # serializer = serializers.RegistrationSerializer(data=request.data)
    # data = {}
    # if serializer.is_valid():
    #     account = serializer.save()
    #     data['success'] = "Successfully registered new user"
    #     data['email'] = account.email
    #     data['first_name'] = account.first_name
    #     data['last_name'] = account.last_name
    #     return_status = status.HTTP_201_CREATED
    # else:
    #     data = serializer.errors
    #     return_status = status.HTTP_400_BAD_REQUEST
    # return Response(serializer.errors, status=return_status)

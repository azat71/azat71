from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.api.serializers import RegistrationSerializer
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from user.models import User


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():

            account = serializer.save()
            data = serializer.data
            data['response'] = 'Успешно зарегистрирован новый пользователь'
            token = Token.objects.get(user=account).key
            data['token'] = token

            return Response(data)
            # data['email'] = account.email
            # data['username'] = account.username
            # data['phone'] = account.phone
            #
        else:
            data = serializer.errors
        return Response(data)



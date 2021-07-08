from django.shortcuts import render
from .models import CashBack, CashAdd
from .serializers import CashbackSerializers, CashbackAddSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from user.permissions import IsAdminUser, IsSeller, IsClient


class CashBackApiView(ListCreateAPIView):
    serializer_class = CashbackSerializers
    queryset = CashBack.objects.all()
    permission_classes = (IsAdminUser | IsSeller,)


class CashAddApiView(ListCreateAPIView):
    serializer_class = CashbackAddSerializers
    queryset = CashAdd.objects.all()
    # permission_classes = (IsAdminUser | IsSeller)

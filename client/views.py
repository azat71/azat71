from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from client.models import Client
from client.serializers import ClientSerializer
from user.permissions import IsAdminUser, IsSeller, IsClient


class ClientListApiView(ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (IsClient,)


class ClientCreateAPIView(CreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (IsAdminUser,)


class ClientUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (IsClient,)


class ClientDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (IsAdminUser,)
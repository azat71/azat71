from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from sale.models import Sale, SaleProduct
from sale.serializers import SaleSerializer, SaleProductSerializer
from user.permissions import IsAdminUser, IsSeller, IsClient


class SaleListApiView(ListAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    permission_classes = (IsClient,)


class SaleCreateAPIView(CreateAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    permission_classes = (IsAdminUser | IsSeller,)


class SaleUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    permission_classes = (IsAdminUser | IsSeller,)


class SaleDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    permission_classes = (IsAdminUser | IsSeller,)


class SaleProductListApiView(ListAPIView):
    serializer_class = SaleProductSerializer
    queryset = SaleProduct.objects.all()
    permission_classes = (IsClient | IsAdminUser,)


class SaleProductCreateAPIView(CreateAPIView):
    serializer_class = SaleProductSerializer
    queryset = SaleProduct.objects.all()
    permission_classes = (IsAdminUser | IsSeller,)


class SaleProductUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = SaleProductSerializer
    queryset = SaleProduct.objects.all()
    permission_classes = (IsAdminUser | IsSeller,)


class SaleProductDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = SaleProductSerializer
    queryset = SaleProduct.objects.all()
    permission_classes = (IsAdminUser | IsSeller,)

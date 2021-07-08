from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from product.models import Product, TypeProduct, Category
from product.serializers import ProductSerializer, TypeProductSerializer, CategorySerializer
from user.permissions import IsAdminUser, IsSeller, IsClient


class ProductListApiView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsClient,)


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAdminUser, IsSeller)


class ProductUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAdminUser, IsSeller)


class ProductDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAdminUser, IsSeller)


class TypeProductListApiView(ListAPIView):
    serializer_class = TypeProductSerializer
    queryset = TypeProduct.objects.all()
    permission_classes = (IsClient,)


class TypeProductCreateAPIView(CreateAPIView):
    serializer_class = TypeProductSerializer
    queryset = TypeProduct.objects.all()
    permission_classes = (IsAdminUser, IsSeller)


class TypeProductUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = TypeProductSerializer
    queryset = TypeProduct.objects.all()
    permission_classes = (IsAdminUser, IsSeller)


class TypeProductDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = TypeProductSerializer
    queryset = TypeProduct.objects.all()
    permission_classes = (IsAdminUser, IsSeller)


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsClient,)


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAdminUser, IsSeller)


class CategoryUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAdminUser, IsSeller)


class CategoryDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAdminUser, IsSeller)
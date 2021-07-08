from rest_framework import serializers
from product.models import Product, Category, TypeProduct


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects, slug_field='name')
    type_product = serializers.SlugRelatedField(queryset=TypeProduct.objects, slug_field='name')

    class Meta:
        model = Product
        fields = "__all__"
    # product_list = serializers.BooleanField(required=False, read_only=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TypeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProduct
        fields = "__all__"
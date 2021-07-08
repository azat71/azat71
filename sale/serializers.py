from rest_framework import serializers
from sale.models import *
from product.models import Product


class SaleProductSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(queryset=Product.objects, slug_field='title')

    class Meta:
        model = SaleProduct
        fields = ('id', 'sale', 'product', 'amount', 'date', 'final_price')
        read_only_fields = ('sale', 'final_price')


class SaleSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(queryset=Product.objects, slug_field='title')

    class Meta:
        model = Sale
        fields = ('id', 'total_cost', 'branch', 'client', 'products')
        read_only_fields = ('total_cost',)

    products = SaleProductSerializer(many=True, required=True)

    def create(self, validated_data):
        sale_products = validated_data.pop('products')
        total_cost = 0
        sale = super().create(validated_data)
        sale_products_to_create = []
        for sale_product in sale_products:
            price = sale_product['product'].price
            amount = sale_product['amount']
            final_price = price * amount
            sale_products_to_create.append(
                SaleProduct(sale=sale, product=sale_product['product'], amount=amount, final_price=final_price)
            )
            total_cost += final_price
        SaleProduct.objects.bulk_create(sale_products_to_create)
        sale.total_cost = total_cost
        cash_product = Product.percent_cashback
        cash_sale = Sale.total_cost
        cashback = (cash_product * cash_sale) / 100
        cashback.save()
        sale.save()

        return sale,cashback

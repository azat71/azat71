from rest_framework import serializers
from .models import CashBack, CashAdd


class CashbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = CashBack
        fields = "__all__"


class CashbackAddSerializers(serializers.ModelSerializer):
    class Meta:
        model = CashAdd
        fields = ('id', 'cash_add', 'total_cash')


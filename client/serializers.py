from rest_framework import serializers
from client.models import *


class ClientSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects, slug_field='username')

    class Meta:
        model = Client
        fields = "__all__"

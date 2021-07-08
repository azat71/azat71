from rest_framework import serializers
from branch.models import *


class BranchSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects, slug_field='username')

    class Meta:
        model = Branch
        fields = "__all__"

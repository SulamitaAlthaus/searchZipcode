
from rest_framework import serializers
from .models import ZipCode


class ZipCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ZipCode
        fields = '__all__'

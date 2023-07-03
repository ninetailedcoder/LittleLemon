from rest_framework import serializers
from .models import booking,menu

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'
        
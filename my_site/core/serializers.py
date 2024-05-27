from rest_framework import serializers

from core import models

class Programmer(serializers.ModelSerializer):
    class Meta:
        model = models.Programmer
        fields = '__all__'
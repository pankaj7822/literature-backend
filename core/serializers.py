# serializers.py
from rest_framework import serializers

from .models import Literature

class LiteratureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Literature
        fields = '__all__'
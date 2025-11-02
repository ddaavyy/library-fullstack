from rest_framework import serializers
from .models import LivrosModel

class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivrosModel
        fields = '__all__'

from rest_framework import serializers
from .models import Files

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['email', 'audio1', 'audio2', 'audio3', 'audio4', 'audio5', ]
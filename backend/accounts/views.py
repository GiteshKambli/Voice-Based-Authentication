from .serializers import FilesSerializer
from .models import Files
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import viewsets
import numpy as np
import json
from bson import Binary
from django.db.models.signals import pre_save

class FilesViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

def upload_voice(request):   
    user_voice = Files() 
    try:
        if request.method == 'POST':           
            email = request.POST.get('email')
            audio1 = request.FILES.get('audio1')
            audio2 = request.FILES.get('audio2')
            audio3 = request.FILES.get('audio3')
            audio4 = request.FILES.get('audio4')
            audio5 = request.FILES.get('audio5')
            user_voice = Files.objects.create(email=email, audio1 = audio1, audio2 = audio2, audio3 = audio3, audio4 = audio4, audio5 = audio5)
    except:
        pass
    finally:
        user_voice.save(commit=False) 
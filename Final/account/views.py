from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Files

# Create your views here.
def signup(request):
    return render(request, 'index.html')

@csrf_exempt
def record(request):
    if request.method == "POST":
        audio1 = request.FILES.get('audio1')
        audio2 = request.FILES.get('audio2')
        audio3 = request.FILES.get('audio3')
        audio4 = request.FILES.get('audio4')
        audio5 = request.FILES.get('audio5')
        audio6 = request.FILES.get('audio6')
        audio7 = request.FILES.get('audio7')
        audio8 = request.FILES.get('audio8')
        audio9 = request.FILES.get('audio9')
        audio10 = request.FILES.get('audio10')
        user_voice = Files.objects.create(audio1 = audio1, audio2 = audio2, audio3 = audio3, audio4 = audio4, audio5 = audio5, audio6 = audio6, audio7 = audio7, audio8 = audio8, audio9 = audio9, audio10 = audio10)
        user_voice.save()
    return render(request, 'record.html')

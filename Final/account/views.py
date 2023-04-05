from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup(request):
    return render(request, 'index.html')

def record(request):
    return render(request, 'record.html')

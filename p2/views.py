from django.shortcuts import render, redirect, HttpResponse
#from django.http import HttpResponse, HttpResponseNotFound
from .models import Files, Name
from .preprocess_audio import get_mel
from .predict import VAuthModel
from .forms import UploadFiles
from .settings import MEDIA_ROOT, BASE_DIR
import numpy as np
from ast import literal_eval
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from pathlib import Path






import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import time
def recorder(file_path, name):
# Sampling frequency
    freq = 44100
    
    # Recording duration
    duration = 5
    
    # Start recorder with the given values
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=2)
    

    # Record audio for the given number of seconds
    sd.wait()

    
    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    #write("recording0.wav", freq, recording)
    
    # Convert the NumPy array to audio file
    wv.write('media/'+file_path+name+'.wav'.format(file_path, name), recording, freq, sampwidth=2)


val = None
@csrf_exempt
def register_info(request):
    
    
    f = Files()
    f.email = request.session.get('email')
    if request.method=='POST':        
        f.audio0 = request.FILES.get('audio0')
        f.audio1 = request.FILES.get('audio1')
        f.audio2 = request.FILES.get('audio2')
        f.audio3 = request.FILES.get('audio3')
        f.audio4 = request.FILES.get('audio4')
        f.audio5 = request.FILES.get('audio5')
        f.audio6 = request.FILES.get('audio6')
        f.audio7 = request.FILES.get('audio7')
        f.audio8 = request.FILES.get('audio8')
        f.audio9 = request.FILES.get('audio9')
        model = VAuthModel()
        #print(type(f.audio0))
        f.embeddings0 = str(model.get_embeddings(get_mel(f.audio0)))
        f.embeddings1 = str(model.get_embeddings(get_mel(f.audio1)))
        f.embeddings2 = str(model.get_embeddings(get_mel(f.audio2)))
        f.embeddings3 = str(model.get_embeddings(get_mel(f.audio3)))
        f.embeddings4 = str(model.get_embeddings(get_mel(f.audio4)))
        f.embeddings5 = str(model.get_embeddings(get_mel(f.audio5)))
        f.embeddings6 = str(model.get_embeddings(get_mel(f.audio6)))
        f.embeddings7 = str(model.get_embeddings(get_mel(f.audio7)))
        f.embeddings8 = str(model.get_embeddings(get_mel(f.audio8)))
        f.embeddings9 = str(model.get_embeddings(get_mel(f.audio9)))
        f = Files.objects.create(
            email = f.email,
            audio0 = f.audio0,
            audio1 = f.audio1,
            audio2 = f.audio2,
            audio3 = f.audio3,
            audio4 = f.audio4,
            audio5 = f.audio5,
            audio6 = f.audio6,
            audio7 = f.audio7,
            audio8 = f.audio8,
            audio9 = f.audio9,
            embeddings0 = f.embeddings0,
            embeddings1 = f.embeddings1,
            embeddings2 = f.embeddings2,
            embeddings3 = f.embeddings3,
            embeddings4 = f.embeddings4,
            embeddings5 = f.embeddings5,
            embeddings6 = f.embeddings6,
            embeddings7 = f.embeddings7,
            embeddings8 = f.embeddings8,
            embeddings9 = f.embeddings9
            )
        f.save()
        
        return HttpResponse('Successfully added audio files')
        #return render(request, 'success.html', {})
    return render(request, 'record.html', {})




def audio_authenticate(request):
    ok = 0
    not_ok = 0
    
    f = VAuthModel()
    if request.method=='POST':
        user = request.POST.get('email')

        n = Name()
        n = Name.objects.filter(email=user)
        if len(n)==1:
            #audio = request.FILES.get('audio')
            audio = recorder(file_path='check/{}'.format(user), name='audio')
            checker = f.get_embeddings(get_mel('media/check/{}audio.wav'.format(user)))
            #print(checker)
            for x in n.values():
                a0 = x.get('embeddings0')
                ans0=f.predict(np.fromstring(a0.strip('[]'), dtype='float32', sep=' ', count=-1),checker)
                if(ans0):
                    ok+=1
                else:
                    not_ok+=1
                a1 = x.get('embeddings1')
                ans1=f.predict(np.fromstring(a1.strip('[]'), dtype='float32', sep=' ', count=-1),checker)
                if(ans1):
                    ok+=1
                else:
                    not_ok+=1
                a2 = x.get('embeddings2')
                ans2=f.predict(np.fromstring(a2.strip('[]'), dtype='float32', sep=' ', count=-1),checker)
                if(ans2):
                    ok+=1
                else:
                    not_ok+=1
                a3 = x.get('embeddings3')
                ans3=f.predict(np.fromstring(a3.strip('[]'), dtype='float32', sep=' ', count=-1),checker)
                if(ans3):
                    ok+=1
                else:
                    not_ok+=1
                a4 = x.get('embeddings4')
                ans4=f.predict(np.fromstring(a4.strip('[]'), dtype='float32', sep=' ', count=-1),checker)
                if(ans4):
                    ok+=1
                else:
                    not_ok+=1
                a5 = x.get('embeddings5')
                ans5=f.predict(np.fromstring(a5.strip('[]'), dtype='float32', sep=' ', count=-1),checker)
                if(ans5):
                    ok+=1
                else:
                    not_ok+=1
                a6 = x.get('embeddings6')
                ans6=f.predict(np.fromstring(a6.strip('[]'), dtype='float32', sep=' ', count=-1),checker)
                if(ans6):
                    ok+=1
                else:
                    not_ok+=1
                a7 = x.get('embeddings7')
                ans7=f.predict(np.fromstring(a7.strip('[]'), dtype='float32', sep=' ', count=-1),checker)
                if(ans7):
                    ok+=1
                else:
                    not_ok+=1
                a8 = x.get('embeddings8')
                ans8=f.predict(np.fromstring(a8.strip('[]'), dtype='float32', sep=' ', count=-1),checker)
                if(ans8):
                    ok+=1
                else:
                    not_ok+=1
                a9 = x.get('embeddings9')
                ans9=f.predict(np.fromstring(a9.strip('[]'), dtype='float32', sep=' ', count=-1),checker)
                if(ans9):
                    ok+=1
                else:
                    not_ok+=1
                
                print(ok, not_ok)
                
                if(ok>=not_ok):
                    return render(request, 'login.html', context = {"message" : "You are authenticated", "value" : False})
                else:
                    return render(request, 'login.html', context = {"message" : "Authentication Failed", "value" : True})
            else:
                return render(request, 'login.html', context = {"message" : "Email not present in databse. Please register yourself first"})
            
    return render(request, 'login.html', {"value" : True})      


def user_authenticate(request, template='index.html'):
    if request.method=='POST':
        if request.POST.get('form_type') == 'formone':
            f = Files()
            phone = request.POST.get('Phone')
            f = Files.objects.filter(phone_no=phone)
            if(len(f)==1):
                # return render(request, 'audio.html', {})
                return HttpResponse('User present')
            else:
                return HttpResponse('please login')
        elif request.POST.get('form_type') == 'formtwo':
            return HttpResponse('Form Two')
        
            
        
    return render(request, 'index.html', {})




def main(request):
    f = Name()
    
    if request.method == "POST":
        
        request.session.modified = True
        email = request.POST.get('email')
        request.session['email'] = email
        x = Name.objects.filter(email=email)
        if len(x)==0:
        
            audio0 = recorder(file_path=str(email), name='audio0')
            audio1 = recorder(file_path=str(email), name='audio1')
            audio2 = recorder(file_path=str(email), name='audio2')
            audio3 = recorder(file_path=str(email), name='audio3')
            audio4 = recorder(file_path=str(email), name='audio4')
            audio5 = recorder(file_path=str(email), name='audio5')
            audio6 = recorder(file_path=str(email), name='audio6')
            audio7 = recorder(file_path=str(email), name='audio7')
            audio8 = recorder(file_path=str(email), name='audio8')
            audio9 = recorder(file_path=str(email), name='audio9')
            model = VAuthModel()
            #print(type(f.audio0))
            f.embeddings0 = str(model.get_embeddings(get_mel('media/{}audio0.wav'.format(email))))
            f.embeddings1 = str(model.get_embeddings(get_mel('media/{}audio1.wav'.format(email))))
            f.embeddings2 = str(model.get_embeddings(get_mel('media/{}audio2.wav'.format(email))))
            f.embeddings3 = str(model.get_embeddings(get_mel('media/{}audio3.wav'.format(email))))
            f.embeddings4 = str(model.get_embeddings(get_mel('media/{}audio4.wav'.format(email))))
            f.embeddings5 = str(model.get_embeddings(get_mel('media/{}audio5.wav'.format(email))))
            f.embeddings6 = str(model.get_embeddings(get_mel('media/{}audio6.wav'.format(email))))
            f.embeddings7 = str(model.get_embeddings(get_mel('media/{}audio7.wav'.format(email))))
            f.embeddings8 = str(model.get_embeddings(get_mel('media/{}audio8.wav'.format(email))))
            f.embeddings9 = str(model.get_embeddings(get_mel('media/{}audio9.wav'.format(email))))
            f = Name.objects.create(
                email = email,
                embeddings0 = f.embeddings0,
                embeddings1 = f.embeddings1,
                embeddings2 = f.embeddings2,
                embeddings3 = f.embeddings3,
                embeddings4 = f.embeddings4,
                embeddings5 = f.embeddings5,
                embeddings6 = f.embeddings6,
                embeddings7 = f.embeddings7,
                embeddings8 = f.embeddings8,
                embeddings9 = f.embeddings9
                )
            f.save()
            contex = {"message" : 'Successfullt signed up', "value" : True}
            return render(request, 'main.html', contex)
        else:
            return HttpResponse("User already present. Please login")
    return render(request, 'main.html')

@csrf_exempt
def k1(request):
    return render(request, 'k1.html')

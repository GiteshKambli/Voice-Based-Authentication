from django import forms

class UploadFiles(forms.Form):
    phone_no = forms.IntegerField()
    email = forms.EmailField()
    audio0 = forms.FileField()
    audio1 = forms.FileField()
    audio2 = forms.FileField()
    audio3 = forms.FileField()
    audio4 = forms.FileField()
    audio5 = forms.FileField()
    audio6 = forms.FileField()
    audio7 = forms.FileField()
    audio8 = forms.FileField()
    audio9 = forms.FileField()
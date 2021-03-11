from django.shortcuts import render
from . import forms

def studentregisterview(request):
    form = forms.StudentRegistration()
    return render(request,'testapp/register.html',{'form':form})
# Create your views here.

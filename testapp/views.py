from django.shortcuts import render
from . import forms

def studentregisterview(request):
    form = forms.StudentRegistration()
    if request.method == 'POST':
        form =forms.StudentRegistration(request.POST)
        if form.is_valid():
            print("form validation success")
            #how to capture a data input from the use
            print('student name',form.cleaned_data['name'])
            print('student roll number',form.cleaned_data['roll'])
            print('student email id',form.cleaned_data['email'])
            print('student feedback',form.cleaned_data['feedback'])

    return render(request,'testapp/register.html',{'form':form})
 

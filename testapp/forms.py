from django import forms
class StudentRegistration(forms.Form):
    name=forms.CharField()
    roll = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)


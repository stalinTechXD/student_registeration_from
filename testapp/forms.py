from django import forms
from django.core import validators
class StudentRegistration(forms.Form):
    name=forms.CharField()
    roll = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)

def starts_with_d(value):
    if value[0].lower() != 'd':
        raise forms.ValidationError('name should be starts with d')
    #if value.alpha() != True:
     #   raise forms.ValidationError("it should be start with alphbet")  
class FeedBackForm(forms.Form):
    name = forms.CharField(validators=[starts_with_d])
    rollno = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label = 'password(again)',widget=forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])   
    bot_handler = forms.CharField(required=False , widget=forms.HiddenInput)
    
    def clean(self):
        cleaned_data = super().clean()
        bot_handler_value = cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError("thanks bot!!")
 #   def clean_name(self):
  #      inputname  = self.cleaned_data['name']
   #     if len(inputname)<4:
    #        raise forms.ValidationError("the length of name field")
     #   return inputname

    #def clean_roll(self):
     #   inputname = self.cleaned_data['rollno']
      #  print("validating roll number")
       # return inputname  
    #def clean_roll(self):
    #    inputname = self.cleaned_data['email']
     #   print("validating roll number")
      #  return inputname  
   # def clean_roll(self):
    #    inputname = self.cleaned_data['feedback']
     #   print("validating roll number")
      #  return inputname          





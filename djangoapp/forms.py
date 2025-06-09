from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.forms import User



#class SignupForm(forms.Form):
    #class Meta:
        #model = Tourusr
        #fields = ['first_name','last_name','username','contact','email','password']

#class SigninForm(forms.Form):
    #class Meta:
        #model = Tourusr
        #fields = ['username','password']

class RegisterForm(forms.Form):
    class Meta:
        model = Vendor
        fields = ['comapny_name','email','password']
class SigninForm(forms.Form):
    class Meta:
        model = Vendor
        fields = ['email','password']
class PackRegForm(forms.Form):
    class Meta:
        model = PackReg
        fields = ['amount','package','days','img']



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']

class SigninForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
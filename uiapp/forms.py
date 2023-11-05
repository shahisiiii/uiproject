from django import forms
from uiapp.models import RegisterModel
from django.contrib.auth.models import User

class StudentRegistration(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email=forms.EmailField()
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)


class RegisterModelForm(forms.ModelForm):
    class Meta:
        models=RegisterModel
        fields="__all__"


class SignUpForm(forms.ModelForm):
    class Meta:
        model=User 
        fields=["first_name","last_name","email","username","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"})
        }

class SignInForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
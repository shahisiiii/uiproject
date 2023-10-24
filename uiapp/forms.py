from django import forms
from uiapp.models import RegisterModel

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
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from uiapp.models import RegisterModel

# Create your views here.


def mainpage(request):
    return render(request,'main.html')

def childpage(request):
    return render(request,'child.html')

# def registration(request):
#     if request.method=="POST":
#         print(request.POST["fisrtname"])
#         print(request.POST["lastname"])
#         print(request.POST["email"])
#         print(request.POST["username"])
#         print(request.POST["password"])
#         return render(request,'registration.html')
#     else:
#         return render(request,'registration.html')

        
class registration(View):

    def get(self,request,*args,**kwargs):
        return render(request,'registration.html')
    
    def post(self,request,*args, **kwargs):
        print(request.POST)
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        RegisterModel.objects.create(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
        return HttpResponse('saved')


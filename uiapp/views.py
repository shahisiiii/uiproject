from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View

from uiapp.models import RegisterModel
from uiapp.forms import StudentRegistration
from uiapp.forms import RegisterModelForm
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
        return redirect('logname')

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')

class StudentReg(View):
    def get(self,request,*args,**kwargs):
        regform=RegisterModelForm()
        return render(request,'studentreg.html',{'data':regform})

class RegisterView(View):
    def get(self,request,*args,**kwargs):
        Viewdata=RegisterModel.objects.all()
        print(Viewdata)
        return render(request,'regview.html',{'data':Viewdata})
    
    def get(self,request,*args,**kwargs):
        Viewdata=RegisterModel.objects.all()
        return render(request,'regview.html',{'data':Viewdata})
    
class RegDelete(View):

     def get(self,request,*args,**kwargs):
        #   print(args)
        #   print(kwargs)
          x = RegisterModel.objects.get(id=kwargs['id'])
        #   print(x)
          x.delete()
          return redirect('regview')
    
class RegEdit(View):
     
     def get(self,request,*args,**kwargs):
          
        vwdata= RegisterModel.objects.get(id=kwargs['id'])
        return render(request,'update.html',{'data':vwdata})
     
     def post(self,request,*args,**kwargs):
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
          

            x = RegisterModel.objects.get(id=kwargs["id"])
            print(x)
            x.first_name=firstname
            x.last_name=lastname
            x.email=email
            x.username=username          
            x.password=password
          
            x.save()
            return redirect('regview')



 









        
    

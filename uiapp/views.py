from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from uiapp.models import RegisterModel
from uiapp.forms import StudentRegistration,RegisterModelForm,SignUpForm,SignInForm
from django.core.mail import send_mail,settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

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



class StudentReg(View):
    def get(self,request,*args,**kwargs):
        regform=RegisterModelForm()
        return render(request,'studentreg.html',{'data':regform})
    
class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')

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
            
class EmailSend(View):
    def get(self,request,*args,**kwargs):
        return render(request,"mailsend.html")
    
    def post(self,request,*args,**kwargs):
        sub=request.POST['sub']
        msg=request.POST['msg']
        to=request.POST['email']
        res=send_mail(sub,msg,settings.EMAIL_HOST_USER,[to])
        if res==1:
            x="mail send succssfuly"
        else:
            x="something went wrong"
        return HttpResponse(x)

class SignUp(View):
    def get(self,request,*args,**kwargs):
        form=SignUpForm()
        return render(request,"signup.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            # form.save()
            User.objects.create_user(**form.cleaned_data)
            return HttpResponse("saved")
    

class SignIn(View):
    def get(self,request,*args,**kwargs):
        form=SignInForm()
        return render(request,"signin.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=SignInForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get("username")
            pass_word=form.cleaned_data.get("password")
            user=authenticate(request,username=user_name,password=pass_word)
            if user:
                login(request,user)
                return HttpResponse("login successfuly")
            else:
                return HttpResponse("invalid credential")






        
    

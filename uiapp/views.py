from django.shortcuts import render

# Create your views here.


def mainpage(request):
    return render(request,'main.html')

def childpage(request):
    return render(request,'child.html')

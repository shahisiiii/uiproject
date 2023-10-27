"""
URL configuration for uiproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from uiapp import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main',views.mainpage,name='mainpage'),
    path('child',views.childpage,name='childpage'),
    # path('reg',views.registration,name='registration.html'),
    path('reg',views.registration.as_view()),
    path('log',views.LoginView.as_view(),name="logname"),
    # path('log',views.StudentRegistration.as_view(),name="logname"),
    path('studentreg',views.StudentReg.as_view()),  
    path('regview',views.RegisterView.as_view()),  

]

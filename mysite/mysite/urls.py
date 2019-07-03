"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import firstapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',firstapp.views.home, name="home"),
    path('echo',firstapp.views.echo, name="echo"),
    path('show',firstapp.views.show, name="show"),
    path('show2',firstapp.views.show2, name="show2"),
    path('length',firstapp.views.length,name="length"),
    path('bigram',firstapp.views.bigram,name="bigram"),
    path('show3',firstapp.views.show3, name="show3"),
    path('fileinput',firstapp.views.fileinput, name="fileinput"),
    path('fileoutput',firstapp.views.fileoutput, name="fileoutput"),
    path('indata',firstapp.views.indata, name="indata"),
    path('outdata',firstapp.views.outdata, name="outdata")
]

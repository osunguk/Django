from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'firstapp/home.html')

def echo(request):
    return render(request, 'firstapp/echo.html')

def show(request):
    inputData = request.GET['inputData']
    return render(request, 'firstapp/show.html',{'inputData':inputData})
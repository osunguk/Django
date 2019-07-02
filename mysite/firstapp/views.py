from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'firstapp/home.html')

#예제 1번
def echo(request):
    return render(request, 'firstapp/echo.html')

def show(request):
    input = request.GET['inputData']
    return render(request, 'firstapp/show.html',{'inputData':input})


#예제 2번
def length(request):
    return render(request, 'firstapp/length.html')

def show2(request):
    lengthData = len(request.GET['lengthData'])
    return render(request, 'firstapp/show2.html', {'lengthData': lengthData})

#예제 3번
def bigram(request):
    return render(request, 'firstapp/bigram.html')

def show3(request):
    biData = str(request.GET['biData'])
    L = []
    for t in biData.split():
        if len(t) <= 1: L.append(t); continue
        for i in range(len(t) - 1):
            L.append(t[i:i + 2])
    ' '.join(L)
    return render(request, 'firstapp/show3.html', {'biData': L})
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

#파일 입출력
def fileinput(request):
    return render(request, 'firstapp/fileinput.html')

def fileoutput(request):
    return render(request, 'firstapp/fileoutput.html')

def indata(request):
    name = request.GET['filename']
    try:

        with open('C:\\Users\osk\Desktop\\tmp\\'+name+'.txt','r') as r:
            readdata = r.read()
    except FileNotFoundError:
        name = '파일이 존재하지 않습니다'
        readdata = ''
    return render(request, 'firstapp/indata.html',{'filename':name, 'readdata':readdata})

def outdata(request):
    title = request.GET['title']
    content = request.GET['content']
    with open('C:\\Users\osk\Desktop\\tmp\\'+title+'.txt','w') as w:
        w.write(content)
    return render(request, 'firstapp/outdata.html',{'title':title ,'content':content})
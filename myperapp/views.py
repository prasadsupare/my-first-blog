from django.shortcuts import render

def text(request):
    return render(request, 'myperapp/home.html')

def contact(request):
    return render(request, 'myperapp/basic.html',{'content':['if you want to contact me','prasadsupare47@gmail.com']})

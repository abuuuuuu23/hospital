from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request,'register.html')

def register1(request):
    if request.method == 'POST'
        name=request.POST.get['name']
        username=request.POST.get['uname']
        phone=request.POST.get['number']
        email=request.POST.get['email']
        date=request.POST.get
from django.shortcuts import *

from myapp.models import Info

# Create your views here.

def index(request):
    return render(request, 'index.html')

def display(request): #data show in displaypage
    obj=Info.objects.all()
    return render(request, 'display.html',{'todolist':obj})

def todo(request):
    a=request.POST.get('fname')
    b=request.POST.get('sdate')
    c=request.POST.get('edate')
    d=request.POST.get('status')
    
    obj=Info(firstname=a,startdate=b,enddate=c,status=d)
    obj.save()
    return redirect('/')

def delete(request):
    a=request.POST.get('id')
    
    obj=Info.objects.filter(id=a)
    obj.delete()
    
    return redirect('/display')

def update(request):
    return render(request, 'update.html')
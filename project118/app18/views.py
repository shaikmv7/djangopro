from django.shortcuts import render
from .models import Employee

# Create your views here.
def showindex(request):
    qs=Employee.objects.all()
    return render(request,'app18/index.html',{'data':qs})


def savedetails(request):
    idno=request.POST.get('idno')
    name=request.POST.get('name')
    photo=request.FILES['photo']
    Employee(idno=idno,name=name,photo=photo).save()
    qs=Employee.objects.all()
    return render(request,'app18/index.html',{'data':qs})


def update(request):
    idno=request.POST.get('idno')
    obj=Employee.objects.get(idno=idno)
    return render(request,'app18/update.html',{'obj':obj})
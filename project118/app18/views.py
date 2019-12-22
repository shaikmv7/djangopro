from django.shortcuts import render
from .models import Employee

# Create your views here.
def autogenid():
    qs=Employee.objects.all()
    if len(qs)==0:
        return 101
    else:
        return (qs[len(qs)-1].idno)+1



def showindex(request):
    qs=Employee.objects.all()
    return render(request,'app18/index.html',{'data':qs,'aid':autogenid()})


def savedetails(request):
    idno=request.POST.get('idno')
    name=request.POST.get('name')
    photo=request.FILES['photo']
    Employee(idno=idno,name=name,photo=photo).save()
    qs=Employee.objects.all()
    return render(request,'app18/index.html',{'data':qs,'aid':autogenid()})


def update(request):
    idno=request.POST.get('idno')
    obj=Employee.objects.get(idno=idno)
    return render(request,'app18/update.html',{'obj':obj,'aid':autogenid()})


def deleteemp(request):
    idno=request.GET['idn']
    Employee.objects.get(idno=idno).delete()
    qs=Employee.objects.all()
    return render(request,'app18/index.html',{'data':qs,'aid':autogenid()})
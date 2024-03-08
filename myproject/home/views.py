from django.shortcuts import render,redirect
from home.models import Employees

def front(request):
    return render(request,'front.html')

def index(request):
    obj = Employees.objects.all()
    return render(request,'index.html',{"emp":obj})

def save(request):
    if request.method == "POST":
        name = request.POST.get('ename')
        age = request.POST.get('eage')
        mobile = request.POST.get('emobile')
        city = request.POST.get('ecity')

        designation = request.POST.get('edesignation')
        query = Employees(name=name, age=age, mobile=mobile, city=city, designation=designation)
        query.save() 
        return redirect("/index")  
    return render(request, 'create.html')


def delete(request,id):
    dlt=Employees.objects.get(id=id)
    dlt.delete()
    return redirect("/index")

def edit(request,id):
    obj=Employees.objects.get(id=id)
    return render(request,'edit.html',{'data':obj})

def update(request,id):
    if request.method=="POST":
        name=request.POST.get('ename')
        age=request.POST.get('eage')
        mobile=request.POST.get('emobile')
        city=request.POST.get('ecity')
        # pic=request.POST.get('epic')
        designation=request.POST.get('edesignation')
        # print(name)
        edit=Employees.objects.get(id=id)
        edit.name=name
        edit.age=age
        edit.mobile=mobile
        edit.city=city

        edit.designation=designation
        edit.save()
    return redirect("/index")
    

def view(request,eid):
    # mydict={}
    one_rec = Employees.objects.get(id=eid)
    # mydict['emp']=one_rec
    # return render(request,'view.html',mydict)
    return render(request,'view.html',{'emp':one_rec})
    

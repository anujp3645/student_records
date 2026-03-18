from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import student,Feedback
# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    error=""
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        admin=auth.authenticate(username=u,password=p)
        try:
            if admin.is_staff:
                auth.login(request,admin)
                error="no" 
        except:
            error="yes"
    d={'error':error}
    return render(request,"login.html",d)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def adminhome(request):
    return render(request,"adminhome.html")
def feedback(request):
    return render(request, "feedback.html")
def add_stu(request):
    error=""
    if request.method == "POST":
        n=request.POST['fname']
        e=request.POST['email']
        c=request.POST['college']
        ct=request.POST['city']
        jd=request.POST['jdate']
        tf=request.POST['tfee']
        pf=request.POST['pfee']
        lf=request.POST['lfee']
        ph=request.POST['phone']
        tech=request.POST['technology']
        img=request.FILES['image']
        try:
            student.objects.create(name=n,email=e,college=c,city=ct,jdate=jd,totalf=tf,paidf=pf,leftf=lf,phone=ph,technology=tech,image=img)
            error="no"
        except:
            error="yes"
    d={"error":error}          

        

    return render(request,"add_students.html",d)

def view_stu(request):
    data=student.objects.all()
    d={'data':data}
    return render(request,"view_stu.html",d)

def del_stu(request,id):
    data=student.objects.get(id=id)
    data.delete()
    return redirect('view_stu')

def edit_stu(request,id):
    data=student.objects.get(id=id)
    error=""
    if request.method == "POST":
        n=request.POST['fname']
        e=request.POST['email']
        c=request.POST['college']
        city=request.POST['city']
        jd=request.POST['jdate']
        tf=request.POST['tfee']
        pf=request.POST['pfee']
        lf=request.POST['lfee']
        ph=request.POST['phone']
        tech=request.POST['technology']

        data.name=n
        data.email=e
        data.college=c
        data.city=city
        data.jdate=jd
        data.totalf=tf
        data.paidf=pf
        data.phone=ph
        data.technology=tech
        try:
            data.save()
            error="no" 
        except:
            error="yes"

    d={"data":data,"error":error}
    return render(request,"edit_student.html",d)

def  search_data(request):
    return render(request,"search_stu.html")

def search_stu(request):
    n=request.POST['name']
    data=student.objects.filter(name_iconation=n)
    d={'data':data}
    return render(request,"view_stu.html",d)

def change_pass(request):
    return render(request,'change_password.html')


    
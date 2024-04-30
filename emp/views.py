from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Emp,Testimonial
from .forms import FeedbackForm
# User name:-Shanish
# Password:-Shanish@123
# Create your views here.
def home(request):
    # return HttpResponse("Welcome to Home Page")
    emps=Emp.objects.all()
    print(emps)
    return render(request,'home.html',{
        'emps':emps
    })

def add_emp(request):
    if request.method=='POST':
        # Fetching data
        emp_name=request.POST.get("name")
        emp_id=request.POST.get("emp_id")
        print(emp_id)
        emp_phone=request.POST.get("mobile")
        emp_address=request.POST.get("address")
        emp_working=request.POST.get("working")
        emp_departement=request.POST.get("departement")

        # Validations

        # Creating data model and set the data
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_departement
        if emp_working is None:
            e.is_working=False
        else:
            e.is_working=True

        # save the data
        e.save()
        # preparing msg
        print("Data is save Successfully")
        return redirect("/")
    return render(request,'addemp.html')

def delete(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect('/')


def update(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,'update.html',{
       'emp':emp 
    })

def do_update(request,emp_id):
    if request.method=='POST':
        # Fetching data
        emp_name=request.POST.get("name")
        emp_id_temp=request.POST.get("emp_id")
        print(emp_id)
        emp_phone=request.POST.get("mobile")
        emp_address=request.POST.get("address")
        emp_working=request.POST.get("working")
        emp_departement=request.POST.get("departement")

        e=Emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_departement
        if emp_working is None:
            e.is_working=False
        else:
            e.is_working=True

        e.save()
    return redirect('/')

def test(request):
    testi=Testimonial.objects.all()
    return render(request,'testimonis.html',{
        'testi':testi
    })

def feedback(request):
    form=FeedbackForm()
    if request.method=='POST':
        print(request.POST)
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'feedback.html',{
        'form': form
    })
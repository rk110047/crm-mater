from django.shortcuts import render,redirect
from .models import *
from django.views import generic
from django.urls import reverse_lazy
from .models import User,EmployeeProfile
from django.contrib.auth import authenticate,login,get_user_model
from rest_framework import generics
from rest_framework.response import Response
from .forms import *


#################################################### F R O N T    E N D   VIEWS ##################

def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign-in')
    
    context = {'form':form}
    return render(request,'profile/register.html',context)
    

def login(request):
    context = {}
    return render(request,'profile/login.html',context)

def profile(request):
    return render(request,'profile/dashboard.html')

def customer(request):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request,'profile/customer.html',context)

def customerinfo(request,pk):
    customer = Customer.objects.get(id=pk)
    return render(request,'profile/custinfo.html',{'customer':customer})


def company(request):
    companies = Company.objects.all()
    context ={'companies':companies}
    return render(request,'profile/company.html',context)

def compinfo(request,pk):
    company = Company.objects.get(id=pk)
    return render(request,'profile/compinfo.html',{'company':company})


def employee(request):
    employees = EmployeeProfile.objects.all()
    context ={'employees':employees}
    return render(request,'profile/employee.html',context)
    
def empinfo(request,pk):
    employee = EmployeeProfile.objects.get(id=pk)
    return render(request,'profile/empinfo.html',{'employee':employee})


def vendor(request):
    vendors = Vendor.objects.all()
    context ={'vendors':vendors}
    return render(request,'profile/vendor.html',context)

def vendinfo(request,pk):
    vendor = Vendor.objects.get(id=pk)
    return render(request,'profile/vendinfo.html',{'vendor':vendor})



def finance(request):
    return render(request,'finance/dashboard.html')

def hr(request):
    return render(request,'hr/dashboard.html')

def payroll(request):
    return render(request,'payroll/dashboard.html')

def project(request):
    return render(request,'project/dashboard.html')


def sla(request):
    return render(request,'sla/dashboard.html')


class indexview(generic.ListView):
    template_name = 'profile/index.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        return User.objects.all()

class detailsview(generic.DetailView):
    model = User
    template_name = 'profile/details.html'


class usercreate(generic.CreateView):
    model = User
    fields = '__all__'

class userupdate(generic.UpdateView):
    model = User
    fields = '__all__'

class userdelete(generic.DeleteView):
    model = User
    success_url = reverse_lazy('index')






from django.shortcuts import render,redirect
from .models import *
from .forms import *


def service(request):
    return render(request,'service/dashboard.html')



####################################################

def plan(request):
    plans = Plan.objects.all()
    context = {'plans':plans}
    return render(request,'service/plan.html',context)


def planinfo(request,pk):
    plan = Plan.objects.get(id=pk)
    return render(request,'service/planinfo.html',{'plan':plan})


def CreatePlan(request):
    plan_form = PlanForm()
    if request.method == 'POST':
        plan_form = PlanForm(request.POST)
        if plan_form.is_valid():
            plan_form.save()

            return redirect('plan')
    
    context = {'plan_form':plan_form}
    return render(request,'service/plan_form.html',context)

def updatePlan(request,pk):  
    plan = Plan.objects.get(id=pk)
    plan_form = PlanForm(instance=plan)
    if request.method == 'POST':
        plan_form = PlanForm(request.POST,instance=plan)
        plan_form.save()

        return redirect('plan')

    context = {'plan_form':plan_form} 
    return render(request,'service/plan_form.html',context)

def deletePlan(request,pk):
    item = Plan.objects.get(id=pk)
    if request.method == 'POST':
        item = Plan.objects.get(id=pk)
        item.delete()
        return redirect('plan')

    context = {'item':item}
    return render(request,'service/deleteplan.html',context)

######################################################

def serv(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request,'service/service.html',context)


def servinfo(request,pk):
    service = Service.objects.get(id=pk)
    return render(request,'service/servinfo.html',{'service':service})

def CreateService(request):
    service_form = ServiceForm()
    if request.method == 'POST':
        service_form = ServiceForm(request.POST)
        if service_form.is_valid():
            service_form.save()

            return redirect('serv')
    
    context = {'service_form':service_form}
    return render(request,'service/service_form.html',context)

def updateService(request,pk):  
    service = Service.objects.get(id=pk)
    service_form = ServiceForm(instance=service)
    if request.method == 'POST':
        service_form = ServiceForm(request.POST,instance=service)
        service_form.save()

        return redirect('serv')

    context = {'service_form':service_form} 
    return render(request,'service/service_form.html',context)

def deleteService(request,pk):
    item = Service.objects.get(id=pk)
    if request.method == 'POST':
        item = Service.objects.get(id=pk)
        item.delete()
        return redirect('serv')

    context = {'item':item}
    return render(request,'service/deleteservice.html',context)

########################################################

def product(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'service/product.html',context)


def prodinfo(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'service/prodinfo.html',{'product':product})


def CreateProduct(request):
    product_form = ProductForm()
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()

            return redirect('prod')
    
    context = {'product_form':product_form}
    return render(request,'service/product_form.html',context)

def updateProduct(request,pk):  
    product = Product.objects.get(id=pk)
    product_form = ProductForm(instance=product)
    if request.method == 'POST':
        product_form = ProductForm(request.POST,instance=product)
        product_form.save()

        return redirect('prod')

    context = {'product_form':product_form} 
    return render(request,'service/product_form.html',context)

def deleteProduct(request,pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item = Product.objects.get(id=pk)
        item.delete()
        return redirect('prod')

    context = {'item':item}
    return render(request,'service/deleteproduct.html',context)


    
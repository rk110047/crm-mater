from django.shortcuts import render,redirect
from .forms import * 
from .models import *
    



def payroll(request):
    return render(request,'payroll/dashboard.html')


def empsalary(request):
    packages = EmployeePackage.objects.all()
    context = {'packages':packages}
    return render(request,'payroll/empsalary.html',context)


def empsalinfo(request,pk):
    package = EmployeePackage.objects.get(id=pk)
    return render(request,'payroll/empsalinfo.html',{'package':package})


def createEmpPac(request): # empPack is empsalary; both naming are alike
    pack_form = PackageForm()
    if request.method == 'POST':
        pack_form = PackageForm(request.POST)
        if pack_form.is_valid():
            pack_form.save()

            return redirect('empsal')

    context = {'pack_form':pack_form}

    return render(request,'payroll/empsal_form.html',context)

def updatePack(request,pk):  
    pack = EmployeePackage.objects.get(id=pk)
    pack_form = PackageForm(instance=pack)
    if request.method == 'POST':
        pack_form = PackageForm(request.POST,instance=pack)
        pack_form.save()

        return redirect('empsal')

    context = {'pack_form':pack_form} 
    return render(request,'payroll/empsal_form.html',context)


def deletePack(request,pk):
    item = EmployeePackage.objects.get(id=pk)
    if request.method == 'POST':
        item = EmployeePackage.objects.get(id=pk)
        item.delete()
        return redirect('empsal')

    context = {'item':item}
    return render(request,'payroll/deletesal.html',context)


################################################### Below MonthlySalary Views ##################################

def monthsal(request):
    salaries = MonthlySalary.objects.all()
    context = {'salaries':salaries}
    return render(request,'payroll/monthsal.html',context)


def monthsalinfo(request,pk):
    salary = MonthlySalary.objects.get(id=pk)
    return render(request,'payroll/monthsalinfo.html',{'salary':salary})

def createMonthSal(request): #
    monthsal_form = MonthlySalForm()
    if request.method == 'POST':
        monthsal_form = MonthlySalForm(request.POST)
        if monthsal_form.is_valid():
            monthsal_form.save()

            return redirect('monthsal')

    context = {'monthsal_form':monthsal_form}

    return render(request,'payroll/monthsal_form.html',context)

def updateMonthSal(request,pk):  
    sal = MonthlySalary.objects.get(id=pk)
    monthsal_form = MonthlySalForm(instance=sal)
    if request.method == 'POST':
        monthsal_form = MonthlySalForm(request.POST,instance=sal)
        monthsal_form.save()

        return redirect('monthsal')

    context = {'monthsal_form':monthsal_form} 
    return render(request,'payroll/monthsal_form.html',context)


def deleteMonthSal(request,pk):
    item = MonthlySalary.objects.get(id=pk)
    if request.method == 'POST':
        item = MonthlySalary.objects.get(id=pk)
        item.delete()
        return redirect('monthsal')

    context = {'item':item}
    return render(request,'payroll/deletemonthsal.html',context)
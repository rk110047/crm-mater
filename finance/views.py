from django.shortcuts import render,redirect
from .models import *
from .serializer import InvoiceSerializer,PurchaseOrderSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics,mixins
from services.models import *
from .forms import *
from .filters import *
from django.db.models.signals import pre_save,post_save


def finance(request):
    return render(request,'finance/dashboard.html')


def invoice(request):
    invoices = Invoice.objects.all()
    invfilter = InvoiceFilter(request.GET,queryset=invoices)
    invoices = invfilter.qs

    # context = {'invoices':invoices,}
    context = {'invoices': invoices, 'invfilter': invfilter}
    return render(request,'finance/invoice.html',context)


def invinfo(request,pk):
    invoice = Invoice.objects.get(id=pk)
    entries = invoice.serviceentry_set.all()
    # s = 0
    # for q in entries.iterator():         ############## need to modify , its wrong here
    #     s += (q.rate * q.Qty) - (((q.Discount)/100) * (q.Qty * q.rate)) + q.Tax
    
    
    context = {'invoice':invoice,'entries':entries} #,'sum': s
    return render(request,'finance/invinfo.html',context)

def createinvoice(request):
    inv_form = InvoiceForm() 
   
    ent_form = SEntryForm()
    if request.method == 'POST':
        inv_form = InvoiceForm(request.POST)
        print("inv_form  :" ,inv_form)
        ent_form = SEntryForm(request.POST)
        if inv_form.is_valid() and ent_form.is_valid():
            inv = inv_form.save()
            # inv.pre_save.connect(pre_save_Stotal, sender=Invoice)
            ent = ent_form.save(False)

            ent.invoice = inv
            ent.save()
            # pre_save.send(sender=Invoice)
            return redirect('invoice')

    context = {'inv_form':inv_form,'ent_form':ent_form}

    return render(request,'finance/invoice_form.html',context)


def updateinvoice(request,pk): # only for updating the invoice,
    invoice = Invoice.objects.get(id=pk)
    # entry = ServiceEntry.objects.get(id=pk)
    inv_form = InvoiceForm(instance=invoice)
    # ent_form = SEntryForm(instance=entry)
    if request.method == 'POST':
        inv_form = InvoiceForm(request.POST,instance=invoice)
        # ent_form = SEntryForm(request.POST,instance=entry)
        if inv_form.is_valid(): #and ent_form.is_valid():
            inv = inv_form.save()
            # ent = ent_form.save(False)

            # ent.invoice = inv
            # ent.save()
            return redirect('invoice')
    context = {'inv_form':inv_form} #,'ent_form':ent_form
    
    return render(request,'finance/updinv_form.html',context)


def updateSEnt(request,pk):  # SERVICE ENTRY
    entry = ServiceEntry.objects.get(id=pk)
    ent_form = SEntryForm(instance=entry)
    if request.method == 'POST':
        ent_form = SEntryForm(request.POST,instance=entry)
        ent = ent_form.save()

        return redirect('invoice')

    context = {'ent_form':ent_form} #,'ent_form':ent_form
    return render(request,'finance/updinvent_form.html',context)


def deleteinvoice(request,pk):
    item = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        item = Invoice.objects.get(id=pk)
        item.delete()
        return redirect('invoice')

    context = {'item':item}
    return render(request,'finance/deleteinv.html',context)

def deleteSEnt(request,pk):
    item = ServiceEntry.objects.get(id=pk)
    # obj = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        item = ServiceEntry.objects.get(id=pk)
        item.delete()
        # obj = Invoice.objects.get(id=pk)
        return redirect('invoice')

    context = {'item':item}
    return render(request,'finance/deleteinv.html',context)



############################################# Below PURCHASE ORDER VIEWS ####################################


def po(request):
    pos = PurchaseOrder.objects.all()
    context = {'pos':pos}
    return render(request,'finance/po.html',context)


def poinfo(request,pk):
    po = PurchaseOrder.objects.get(id=pk)
    entries = po.productentry_set.all()
    s = 0
    for q in entries.iterator():
        s += (q.rate * q.Qty) - (((q.Discount)/100) * (q.Qty * q.rate)) + q.Tax

    context = {'po':po,'entries':entries,'sum': s}
    return render(request,'finance/poinfo.html',context)


def createPO(request):
    po_form = PoForm()
    ent_form = PEntryForm()
    if request.method == 'POST':
        po_form = PoForm(request.POST)
        ent_form = PEntryForm(request.POST)
        if po_form.is_valid() and ent_form.is_valid():
            po = po_form.save()
            ent = ent_form.save(False)

            ent.PO = po
            ent.save()
            return redirect('po')

    context = {'po_form':po_form,'ent_form':ent_form}

    return render(request,'finance/po_form.html',context)


def updatePO(request,pk): # only for updating the invoice, for service entry create another view 
    po = PurchaseOrder.objects.get(id=pk)
    po_form = PoForm(instance=po)
    if request.method == 'POST':
        po_form = PoForm(request.POST,instance=po)
        if po_form.is_valid(): 
            po = po_form.save()
            
            return redirect('po')
    context = {'po_form':po_form} 
    
    return render(request,'finance/updpo_form.html',context)


def updatePEnt(request,pk):  # PRODUCT ENTRY
    entry = ProductEntry.objects.get(id=pk)
    ent_form = PEntryForm(instance=entry)
    if request.method == 'POST':
        ent_form = PEntryForm(request.POST,instance=entry)
        ent = ent_form.save()

        return redirect('po')

    context = {'ent_form':ent_form} #,'ent_form':ent_form
    
    return render(request,'finance/updpoent_form.html',context)


def deletePO(request,pk):
    item = PurchaseOrder.objects.get(id=pk)
    if request.method == 'POST':
        item = PurchaseOrder.objects.get(id=pk)
        item.delete()
        return redirect('po')

    context = {'item':item}
    return render(request,'finance/deletepo.html',context)

def deletePEnt(request,pk):
    item = ProductEntry.objects.get(id=pk)
    # obj = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        item = ProductEntry.objects.get(id=pk)
        item.delete()
        # obj = Invoice.objects.get(id=pk)
        return redirect('po')

    context = {'item':item}
    return render(request,'finance/deletepo.html',context)

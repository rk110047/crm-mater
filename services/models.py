from django.db import models
from finance.models import *

class Service(models.Model) :
    
 
    
    
    # invoice       = models.ForeignKey(Invoice,on_delete=models.CASCADE,null=True)
    serviceId     = models.CharField(max_length=50,null=True,blank=False)
    # name          = models.CharField(max_length=100,blank=False)
    name_c        = models.CharField(verbose_name='company',max_length=100,blank=False,null=True)
    Type          = models.CharField(verbose_name='Type',max_length=20, blank = False,default='Unknown',null = True)
    # code          = models.CharField(max_length=100)
    description   = models.CharField(max_length=100)
    cost          = models.FloatField()
    Active        = models.BooleanField(default='True')
    
    
    def __str__(self):
        return self.serviceId 
    
    

    class Meta:
        verbose_name_plural = 'Service'
        
    

class Plan(models.Model):

    types = (
    ('PREPAID','Prepaid'),
    ('POSTPAID', 'Postpaid'),
    # ('UNKNOWN','Unknown')
    )
    
    planId         = models.CharField(max_length=30,null=True,blank=False)   
    Type           = models.CharField(max_length=20,choices=types,null=True)
    duration       = models.CharField(max_length=20,null = True)
    dateOfCreation = models.DateField(null=True)
    validity       = models.DateField(null=True)
    billingCycle   = models.DateField(null=True)
    dueDate        = models.DateField(null=True)
    terms          = models.TextField(max_length=250,verbose_name='PlanTerms',null=True)

    def __str__(self):
        return self.planId

    class Meta:
        verbose_name_plural = 'plan'
    


class Product(models.Model):
    Product_no          = models.CharField(max_length=30,null=True,blank=False)   
    Product_name        = models.CharField(max_length=20,blank=False,null=True)   
    cost                = models.FloatField()
    # cost                = models.DecimalField(max_digits=20, decimal_places=2, blank=True)
    Company_name        = models.CharField(max_length=20,blank=False)
    Product_Description = models.TextField(max_length=250,null=True)

    def __str__(self):
        return self.Product_no
    
    class Meta:
        verbose_name_plural = 'product'


##################################################################################################

                                                            #--------------------FOR SERVICE INLINE




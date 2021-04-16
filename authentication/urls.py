from django.urls import path
from . import views
from .api import *


urlpatterns = [
    
    
    path('',views.profile,name = 'profile'),
    
    # authentication/
    path('user/', views.indexview.as_view(), name = 'user'),

    path('customer/', views.customer, name = 'customer'),
    path('customer/<pk>/', views.customerinfo, name = 'customerinfo'),

    path('company/', views.company, name = 'company'),
    path('company/<pk>/', views.compinfo, name = 'compinfo'),

    path('employee/', views.employee, name = 'employee'),
    path('employee/<pk>', views.empinfo, name = 'empinfo'),

    path('vendor/', views.vendor, name = 'vendor'),
    path('vendor/<pk>', views.vendinfo, name = 'vendinfo'),


    
    path('register/', views.register, name='sign-up'),
    path('login/', views.login, name='sign-in'),


]
    
    
 



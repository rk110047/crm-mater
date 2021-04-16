from django.forms import ModelForm
from django import forms
from .models import *
from services.models import *
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class DateInput(forms.DateInput):
    input_type = 'date'


# class InvoiceForm(ModelForm):
# 	class Meta:
# 		model = Invoice
# 		fields = '__all__'
# 		widgets = {
            
#             'Invoice_date' : DateInput(),
            
#         }
#         # exclude = []


# class SEntryForm(ModelForm):
# 	class Meta:
# 		model = ServiceEntry
# 		fields = ['service',
#                   'description',
#                   'rate',
#                   'Qty',
#                   'Discount',
#                   'Tax']
        


# class PoForm(ModelForm):
# 	class Meta:
# 		model = PurchaseOrder
# 		fields = '__all__'
#         # exclude = []
    

# class PEntryForm(ModelForm):
# 	class Meta:
# 		model = ProductEntry
# 		fields = ['Product',
#                   'description',
#                   'rate',
#                   'Qty',
#                   'Discount',
#                   'Tax']
#         # exclude = []
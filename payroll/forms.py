from django.forms import ModelForm
from .models import *
from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class DateInput(forms.DateInput):
    input_type = 'date'
	

class PackageForm(ModelForm):
	class Meta:
		model = EmployeePackage
		fields = '__all__'
		widgets = {
            
            'dateOfPayment': DateInput(),
            
        }
        # exclude = []


class MonthlySalForm(ModelForm):
	class Meta:
		model = MonthlySalary
		fields = '__all__'
		widgets = {
            
            'salaryMonth': DateInput(),
            
        }
        # exclude = []
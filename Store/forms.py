from django.core import validators
from django import forms
from .models import User

class ItemsRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['sr_number','choose','name', 'email', 'address', 'products', 'quantity', 'packaging', 'date', 'images' ]
        widgets = {
            'sr_number':forms.TextInput(attrs={'class':'form-control'}),
            'choose':forms.RadioSelect(),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control', "rows":1, "cols":20}),
            'products':forms.Select(), 
            'quantity':forms.TextInput(attrs={'class':'form-control'}), 
            'packaging':forms.CheckboxInput(),
            'date':forms.DateInput(),
            'images':forms.FileInput(),
        }
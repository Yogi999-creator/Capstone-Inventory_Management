from django.core import validators
from django import forms
from .models import User

class ItemsRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['choose','name', 'email', 'address', 'password', 'products' ]
        widgets = {
            'choose':forms.RadioSelect(),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control', "rows":1, "cols":20}),
            'password':forms.PasswordInput( render_value=True ,attrs={'class':'form-control'}),
            'products':forms.Select(),  
        }
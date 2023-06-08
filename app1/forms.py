from typing import Any, Dict
from django import forms
from django.core import validators

class customerRegistration(forms.Form):
    Enter_First_name = forms.CharField(error_messages={'required':'Must fill your name'})
    Middle_name = forms.CharField(required=False)
    Last_name = forms.CharField(required=False)
    
    email = forms.EmailField(label='Enter your email ',validators=[validators.MaxLengthValidator(20)])
    serial = forms.IntegerField(help_text='*', min_value=1)
   # phone_number = forms.IntegerField(widget=forms.HiddenInput())
    password = forms.CharField(widget=forms.PasswordInput(),min_length=8, max_length=15)
    re_password = forms.CharField(widget=forms.PasswordInput(),min_length=8, max_length=15)
    textarea = forms.CharField(widget=forms.Textarea (attrs={'rows':5,'cols':20}))
    Checkbox = forms.CharField(widget=forms.CheckboxInput() )
    payments = forms.DecimalField(min_value=2500,max_value=5000,max_digits=6,decimal_places=2)
    django = forms.BooleanField()



    


    def clean(self):
        cleaned_data = super().clean
        password_match = self.cleaned_data['password']
        re_password_match = self.cleaned_data['re_password']
        if password_match != re_password_match:
            raise forms.ValidationError("Password Doesn't match")
   
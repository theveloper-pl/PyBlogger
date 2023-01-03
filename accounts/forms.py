
from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))
    confirmpassword=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))
    class Meta:
        model = Account
        fields=['first_name','last_name','phone_number','email','password','confirmpassword']
    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs["placeholder"]='First name'
        self.fields['last_name'].widget.attrs["placeholder"]='Last name'
        self.fields['phone_number'].widget.attrs["placeholder"]='Phone Number'
        self.fields['email'].widget.attrs["placeholder"]='E-mail'
        for field in self.fields:
            self.fields[field].widget.attrs["class"]='form-control'
    def clean(self):
        cleander_data = super(RegistrationForm, self).clean()
        password = cleander_data.get("password")
        confirmpassword = cleander_data.get("confirmpassword")
        if password !=confirmpassword:
            raise forms.ValidationError("Password does not match")

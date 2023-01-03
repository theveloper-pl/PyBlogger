from django.shortcuts import render
from django.views.generic import View
from . import forms

class LoginPageView(View):
    template_name = 'login.html'
    form_class = forms.LoginForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, 'login.html', context={'form': form, 'message': message})
        
    # def post(self, request):
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user = auth.authenticate(email=email, password=password)

    #     return render(request, 'login.html', context={'form': form, 'message': message})

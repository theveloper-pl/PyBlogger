from django.shortcuts import render, redirect
from django.views.generic import View
from . import forms
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginPageView(View):
    def get(self, request):
        context = {}
        context['title'] = 'Login'
        context['description'] = 'Thats very useful option !'
        return render(request, 'login.html', context)
        
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('PostListHomeView')
        else:
            return redirect('LoginPageView')

class RegisterPageView(View):
    def get(self, request):
        context = {}
        context['title'] = 'Login'
        context['description'] = 'Thats very useful option !'
        return render(request, 'login.html', context)
        
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('PostListHomeView')
        else:
            return redirect('LoginPageView')

class LogoutPageView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get(self, request):
        auth.logout(request)
        return redirect('LoginPageView')
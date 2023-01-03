from django.shortcuts import render, redirect
from django.views.generic import View
from . import forms
from django.contrib import messages,auth


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

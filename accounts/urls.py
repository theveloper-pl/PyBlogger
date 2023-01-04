from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginPageView.as_view(), name="LoginPageView"),
    path('register/', views.RegisterPageView.as_view(), name="RegisterPageView"),
]

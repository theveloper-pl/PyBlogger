from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListHomeView.as_view(), name="PostListHomeView"),
    path('posts/', views.PostListView.as_view(), name="PostListView"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='PostDetailView'),
]

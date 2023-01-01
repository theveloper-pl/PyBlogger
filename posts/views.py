from django.shortcuts import render
from django.views import generic
from .models import Post



class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'   # your own name for the list as a template variable
    queryset = Post.objects.all()
    template_name = 'home.html'  # Specify your own template name/location
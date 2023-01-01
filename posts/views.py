from django.shortcuts import render
from django.views import generic
from .models import Post



class PostListHomeView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.all()[:3] 
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'IT'
        context['description'] = 'And why its so interesting ?!'
        return context

class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.all()
    paginate_by = 4
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Software Engineering'
        context['description'] = 'And our posts about it !'
        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['description'] = context['object'].short
        return context
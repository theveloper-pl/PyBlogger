from django.shortcuts import render
from django.views import generic



class BookListView(generic.ListView):
    model = Book
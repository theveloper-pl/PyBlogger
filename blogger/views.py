from django.shortcuts import render


def about(request):
    context={'title':"Who am I ?", "description":"And what is this website ?"}
    return render(request,"about.html",context)
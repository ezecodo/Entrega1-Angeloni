from django.shortcuts import render

def homepage(request):
    return render(request, 'inicio/homepage.html')

def about(request):
    return render(request, 'inicio/about.html')

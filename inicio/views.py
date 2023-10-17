from django.shortcuts import render

def homepage(request):
    return render(request, 'inicio/homepage.html')

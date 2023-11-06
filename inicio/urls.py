from django.urls import path
from . import views
from .views import about

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', about, name='about'),
]

from django.urls import path
from . import views

app_name = 'fredapp'

urlpatterns = [
    path('', views.home, name='home'),
]
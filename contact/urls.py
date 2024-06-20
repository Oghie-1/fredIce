from django.urls import path
from . import views


app_name = 'contact' 

urlpatterns = [
    path('', views.contact_list, name='contact-list'),
    path('contact-home', views.contact_home, name='contact-home'),
]
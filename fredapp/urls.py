from django.urls import path
from . import views

app_name = 'fredapp'  # Ensure this matches the namespace used in your include

urlpatterns = [
    path('home', views.homepage, name='home'),  # Root URL for the home page
]

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blogHome, name="blog-home"),
    path('post/<int:id>', views.post_detail, name='blog-detail')
]
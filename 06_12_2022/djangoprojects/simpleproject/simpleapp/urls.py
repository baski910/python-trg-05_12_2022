from django.urls import path
from . import views

# 'simplapp:index'

urlpatterns = [
    path('index',views.index,name='index'),
    path('welcome',views.welcome,name='welcome')
]
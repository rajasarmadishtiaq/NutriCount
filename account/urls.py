from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
import food.views
import network.views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('logs/', food.views.logs, name='logs'),
    path('network/', network.views.my_network, name='network'),
]

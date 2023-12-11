from django.urls import path, include
from . import views

urlpatterns = [
    path('add-food/', views.add_food, name='add_food'),
    path('edit-logs/', views.edit_logs, name='edit_logs'),
]
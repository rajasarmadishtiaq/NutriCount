from django.urls import path, include
from . import views

urlpatterns = [
    path('add-mentor/', views.add_mentor, name='add_mentor'),
    path('remove-mentee-mentor/', views.remove_mentor_or_mentee, name='remove_mentor_or_mentee'),
    path('view-mentee-logs/', views.view_mentee_logs, name='view_mentee_logs'),
]

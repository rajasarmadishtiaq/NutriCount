from django.contrib import admin
from .models import Food, UserMetric


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'calories', 'created_at']


@admin.register(UserMetric)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'calories_consumed']
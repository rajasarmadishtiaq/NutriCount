from django.db import models
from account.models import Profile
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Food(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.FloatField('Calories in kcal')
    serving_size_g = models.FloatField('Serving size')
    fat_total_g = models.FloatField('Fats in grams')
    protein_g = models.FloatField('Proteins in grams')
    carbohydrates_total_g = models.FloatField('Carbs in grams')
    created_at = models.DateField('Created At', default=datetime.date.today)

    def __str__(self):
        return self.name


class FoodSearch(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateField('Created At', default=datetime.date.today)

    def get_saved_foods(self):
        return Food.objects.filter(user=self.user, created_at=self.created_at)


class UserMetric(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateField('Created At', default=datetime.date.today)
    calories_consumed = models.PositiveIntegerField('Calories consumed in kcal', blank=True, null=True)
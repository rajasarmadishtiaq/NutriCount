from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

EXERCISE_CHOICES = [
    (1.2, 'Sedentary'),
    (1.375, 'Lightly active'),
    (1.55, 'Moderately active'),
    (1.725, 'Very active'),
    (1.9, 'Super active')
]

PREFERENCE = [
    (-1000.0, 'Extreme weight loss'),
    (-500.0, 'Moderate weight loss'),
    (-250.0, 'Light weight loss'),
    (0.01, 'Maintaining Weight'),
    (250.0, 'Light weight gain'),
    (500.0, 'Moderate weight gain'),
    (1000.0, 'Extreme weight gain')
]

GENDERS = [
    ('Male', 'Male'),
    ('Female', 'Female')
]


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True)
    weight = models.FloatField('Weight in kg', validators=[MinValueValidator(30), MaxValueValidator(300)], blank=True, null=True)
    height = models.FloatField('Height in cm', validators=[MinValueValidator(55), MaxValueValidator(250)], blank=True, null=True)
    exercise = models.FloatField(max_length=50, choices=EXERCISE_CHOICES, blank=True, null=True)
    age = models.PositiveIntegerField(default=12,
                                      validators=[MinValueValidator(12), MaxValueValidator(100)], blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDERS, blank=True, null=True)
    preference = models.FloatField(choices=PREFERENCE, blank=True, null=True)
    calorie = models.PositiveIntegerField('Calories in kcal', blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

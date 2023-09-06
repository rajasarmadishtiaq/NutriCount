# Generated by Django 4.2.4 on 2023-08-30 13:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_profile_calorie_consumed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='calorie',
            field=models.IntegerField(blank=True, null=True, verbose_name='Calories in kcal'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='calorie_consumed',
            field=models.IntegerField(blank=True, null=True, verbose_name='Calories consumed in kcal'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(55), django.core.validators.MaxValueValidator(250)], verbose_name='Height in cm'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(300)], verbose_name='Weight in kg'),
        ),
    ]
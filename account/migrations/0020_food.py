# Generated by Django 4.2.4 on 2023-08-31 07:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_delete_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('calories', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('carbs', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('proteins', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('fats', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
    ]

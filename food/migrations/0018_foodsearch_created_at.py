# Generated by Django 4.2.4 on 2023-09-01 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0017_foodsearch'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodsearch',
            name='created_at',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.food'),
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-31 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_alter_food_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
    ]
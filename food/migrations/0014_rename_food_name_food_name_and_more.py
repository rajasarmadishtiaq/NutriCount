# Generated by Django 4.2.4 on 2023-08-31 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_remove_food_carbs_remove_food_fats_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='food_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='serving_size',
            new_name='serving_size_g',
        ),
    ]

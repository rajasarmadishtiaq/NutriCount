# Generated by Django 4.2.4 on 2023-08-30 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_calorie_alter_profile_exercise_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='calorie',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_profile_preference_alter_profile_calorie_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='calorie_consumed',
            field=models.IntegerField(blank=True, null=True, verbose_name='in kcal'),
        ),
    ]

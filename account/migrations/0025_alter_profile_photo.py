# Generated by Django 4.2.4 on 2023-09-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_remove_profile_calorie_consumed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='media/default/default.png', null=True, upload_to='users/%Y/%m/%d/'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-31 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[(0, 'Male'), (1, 'Female')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='preference',
            field=models.IntegerField(blank=True, choices=[(-300, 'Extreme weight loss'), (-200, 'Moderate weight loss'), (-100, 'Light weight loss'), (0, 'Maintain Weight'), (100, 'Light weight gain'), (200, 'Moderate weight gain'), (300, 'Extreme weight gain')], null=True),
        ),
    ]
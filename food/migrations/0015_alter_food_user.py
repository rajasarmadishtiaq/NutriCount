# Generated by Django 4.2.4 on 2023-08-31 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_alter_profile_preference'),
        ('food', '0014_rename_food_name_food_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
        ),
    ]

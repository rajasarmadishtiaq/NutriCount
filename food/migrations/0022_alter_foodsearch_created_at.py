# Generated by Django 4.2.4 on 2023-09-02 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0021_alter_foodsearch_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodsearch',
            name='created_at',
            field=models.DateField(default=datetime.date.today, verbose_name='Created At'),
        ),
    ]

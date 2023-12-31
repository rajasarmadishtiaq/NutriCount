# Generated by Django 4.2.4 on 2023-08-31 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0012_alter_food_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='carbs',
        ),
        migrations.RemoveField(
            model_name='food',
            name='fats',
        ),
        migrations.RemoveField(
            model_name='food',
            name='proteins',
        ),
        migrations.AddField(
            model_name='food',
            name='carbohydrates_total_g',
            field=models.FloatField(default=0, verbose_name='Carbs in grams'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='fat_total_g',
            field=models.FloatField(default=0, verbose_name='Fats in grams'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='protein_g',
            field=models.FloatField(default=0, verbose_name='Proteins in grams'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='serving_size',
            field=models.FloatField(default=0, verbose_name='Serving size'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.FloatField(default=0, verbose_name='Calories in kcal'),
            preserve_default=False,
        ),
    ]

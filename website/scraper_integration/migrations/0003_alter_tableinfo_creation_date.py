# Generated by Django 5.0.7 on 2024-07-30 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper_integration', '0002_analyseddata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableinfo',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

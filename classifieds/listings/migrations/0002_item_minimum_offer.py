# Generated by Django 4.0.5 on 2022-06-08 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='minimum_offer',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-11 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingitem',
            name='currency',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]

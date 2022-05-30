# Generated by Django 4.0.4 on 2022-05-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_billingitem_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingitem',
            name='type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Deposit'), (2, 'Charge'), (3, 'Block')], null=True),
        ),
    ]
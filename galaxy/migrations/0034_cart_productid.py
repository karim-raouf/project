# Generated by Django 4.2.4 on 2023-08-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0033_remove_cart_productid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='ProductID',
            field=models.IntegerField(null=True),
        ),
    ]
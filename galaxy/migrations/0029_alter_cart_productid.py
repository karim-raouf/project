# Generated by Django 4.2.4 on 2023-08-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0028_alter_cart_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='ProductID',
            field=models.IntegerField(null=True),
        ),
    ]
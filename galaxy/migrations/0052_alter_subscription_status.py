# Generated by Django 4.2.4 on 2023-09-06 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0051_alter_organization_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='Status',
            field=models.BooleanField(null=True),
        ),
    ]
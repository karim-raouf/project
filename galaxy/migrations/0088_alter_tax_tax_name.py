# Generated by Django 4.2.4 on 2023-11-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0087_alter_organization_subscriptionid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax',
            name='tax_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

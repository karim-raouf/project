# Generated by Django 2.1.15 on 2023-08-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0004_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]

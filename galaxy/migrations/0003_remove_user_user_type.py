# Generated by Django 4.2.4 on 2024-01-06 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0002_language_product_userstype_user_birth_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_Type',
        ),
    ]

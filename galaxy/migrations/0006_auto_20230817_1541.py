# Generated by Django 2.1.15 on 2023-08-17 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0005_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='organization',
        ),
    ]

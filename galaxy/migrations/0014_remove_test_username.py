# Generated by Django 4.2.4 on 2023-08-18 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0013_test_username_alter_test_id_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='username',
        ),
    ]

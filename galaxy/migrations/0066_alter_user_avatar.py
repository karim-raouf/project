# Generated by Django 4.2.4 on 2023-09-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0065_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
    ]

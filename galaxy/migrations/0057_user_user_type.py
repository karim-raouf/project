# Generated by Django 4.2.4 on 2023-09-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0056_rename_instgramlink_organization_instagramlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_Type',
            field=models.IntegerField(choices=[(1, 'Admin-User'), (2, 'System-User')], null=True),
        ),
    ]

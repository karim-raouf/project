# Generated by Django 4.2.4 on 2023-08-31 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0045_remove_user_organizationid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='Org_name',
        ),
    ]
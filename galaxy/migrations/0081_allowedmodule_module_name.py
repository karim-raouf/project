# Generated by Django 4.2.4 on 2023-10-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0080_rename_allowedmodules_allowedmodule'),
    ]

    operations = [
        migrations.AddField(
            model_name='allowedmodule',
            name='module_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

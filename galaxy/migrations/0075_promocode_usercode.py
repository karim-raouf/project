# Generated by Django 4.2.4 on 2023-09-28 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0074_promocode'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocode',
            name='usercode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

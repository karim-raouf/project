# Generated by Django 4.2.4 on 2023-08-23 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0019_account_subscription_delete_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

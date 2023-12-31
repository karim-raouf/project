# Generated by Django 4.2.4 on 2023-08-24 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0022_alter_subscription_planid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrganizationName', models.CharField(max_length=50, null=True)),
                ('CreatedDate', models.DateField(verbose_name='Created Date')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='subscription',
            name='OrganizationID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='galaxy.organization'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-26 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0024_rename_userid_organization_userid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='UserID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='UserID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='OrganizationID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaxy.organization'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='UserID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='OrganizationID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaxy.organization'),
        ),
    ]
# Generated by Django 4.2.4 on 2023-11-21 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0086_tax_tax_name_alter_user_subscriptionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='SubscriptionID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='galaxy.subscription'),
        ),
        migrations.AlterField(
            model_name='user',
            name='SubscriptionID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaxy.subscription'),
        ),
    ]

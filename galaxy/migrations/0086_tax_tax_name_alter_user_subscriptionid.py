# Generated by Django 4.2.4 on 2023-11-21 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0085_alter_timerestriction_day_of_week_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tax',
            name='tax_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='SubscriptionID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='galaxy.subscription'),
        ),
    ]

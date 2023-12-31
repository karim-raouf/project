# Generated by Django 4.2.4 on 2023-10-07 20:14

from django.db import migrations, models
import galaxy.timeformatfield


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0084_timerestriction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timerestriction',
            name='day_of_week',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='timerestriction',
            name='end_time',
            field=galaxy.timeformatfield.TimeFormatField(max_length=12),
        ),
        migrations.AlterField(
            model_name='timerestriction',
            name='start_time',
            field=galaxy.timeformatfield.TimeFormatField(max_length=12),
        ),
    ]

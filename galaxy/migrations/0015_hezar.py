# Generated by Django 4.2.4 on 2023-08-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0014_remove_test_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hezar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hezar_name', models.CharField(max_length=50)),
            ],
        ),
    ]

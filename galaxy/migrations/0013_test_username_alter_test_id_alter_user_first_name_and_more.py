# Generated by Django 4.2.4 on 2023-08-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0012_remove_user_ali'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
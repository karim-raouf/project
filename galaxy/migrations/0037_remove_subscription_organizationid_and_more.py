# Generated by Django 4.2.4 on 2023-08-30 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0036_alter_cart_type_alter_product_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='OrganizationID',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='PlanID',
        ),
        migrations.AddField(
            model_name='subscription',
            name='ProductID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaxy.product'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='Type',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Add-Ones', 'Add-Ones')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='Type',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Add-Ones', 'Add-Ones')], max_length=20, null=True),
        ),
    ]
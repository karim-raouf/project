# Generated by Django 4.2.4 on 2023-08-30 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0039_cart_bundle_t_product_bundle_t_subscription_bundle_t'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='Code',
            field=models.IntegerField(null=True),
        ),
    ]

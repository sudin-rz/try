# Generated by Django 3.2.25 on 2024-03-31 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customer_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='stripe_card_last4',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='stripe_payment_method_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
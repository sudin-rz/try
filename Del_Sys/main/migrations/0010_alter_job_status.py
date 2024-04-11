# Generated by Django 3.2.25 on 2024-04-10 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20240409_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('creating', 'Creating'), ('processing', 'Processing'), ('picking', 'Picking'), ('delivering', 'Delivering'), ('completing', 'Completing'), ('cancelled', 'Cancelled')], default='creating', max_length=20),
        ),
    ]
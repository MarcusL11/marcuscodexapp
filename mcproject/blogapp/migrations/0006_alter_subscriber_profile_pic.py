# Generated by Django 5.0.1 on 2024-01-25 14:14

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_subscriber_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]

# Generated by Django 4.0.2 on 2023-05-08 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_wishlistitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WishlistItem',
        ),
    ]

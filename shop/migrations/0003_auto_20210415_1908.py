# Generated by Django 3.1.7 on 2021-04-15 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210415_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='img',
            new_name='image',
        ),
    ]

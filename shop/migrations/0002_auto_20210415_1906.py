# Generated by Django 3.1.7 on 2021-04-15 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='image',
            new_name='img',
        ),
    ]

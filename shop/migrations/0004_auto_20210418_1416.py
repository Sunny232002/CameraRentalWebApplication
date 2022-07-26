# Generated by Django 3.1.7 on 2021-04-18 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210415_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='address',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='city',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='owner',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='state',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='vendor_email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]

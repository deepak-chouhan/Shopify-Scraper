# Generated by Django 4.0.6 on 2022-07-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopifyScrapper', '0007_alter_size_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='auto_checkout_link',
        ),
        migrations.RemoveField(
            model_name='data',
            name='size',
        ),
        migrations.AddField(
            model_name='data',
            name='product_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='stock_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
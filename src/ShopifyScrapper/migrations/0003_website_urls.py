# Generated by Django 4.0.6 on 2022-07-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopifyScrapper', '0002_remove_website_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='urls',
            field=models.TextField(null=True),
        ),
    ]
# Generated by Django 2.0.7 on 2018-09-19 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180919_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcatagory',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

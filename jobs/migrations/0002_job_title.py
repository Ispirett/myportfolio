# Generated by Django 2.0.6 on 2018-07-04 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='hello', max_length=40),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.0.7 on 2018-09-04 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trinionlinemall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stores',
            name='facebook',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]

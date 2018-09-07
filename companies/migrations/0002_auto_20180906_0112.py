# Generated by Django 2.0.7 on 2018-09-06 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StoreOwners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stores', models.ManyToManyField(to='companies.Stores')),
            ],
        ),
        migrations.AddField(
            model_name='stores',
            name='store_catagory',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='companies.StoreCatagory'),
            preserve_default=False,
        ),
    ]

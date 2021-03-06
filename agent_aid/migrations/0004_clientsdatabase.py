# Generated by Django 2.0.7 on 2018-07-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent_aid', '0003_delete_insuranceproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=50)),
                ('CONTACT', models.CharField(max_length=50)),
                ('OCCUPATION', models.CharField(max_length=100)),
                ('CLIENT_NO', models.IntegerField()),
                ('POLICY_NO', models.IntegerField()),
                ('POLICY_TYPE', models.CharField(max_length=100)),
                ('POLICY_PROPERTIES', models.CharField(max_length=100)),
                ('ISSUE_DATE', models.DateField()),
                ('REVIEW_DATE', models.DateField()),
                ('DOB', models.DateField()),
                ('PREMIUM_AMOUNT', models.FloatField()),
                ('MODE_OF_PAYMENT', models.CharField(max_length=100)),
                ('PDF', models.FileField(upload_to='pdf//%Y/%m/%d/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

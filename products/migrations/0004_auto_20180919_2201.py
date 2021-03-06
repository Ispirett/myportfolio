# Generated by Django 2.0.7 on 2018-09-19 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180912_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='product_catagory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.ProductCatagory'),
            preserve_default=False,
        ),
    ]

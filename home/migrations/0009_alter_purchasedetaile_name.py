# Generated by Django 4.2.4 on 2023-11-01 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedetaile',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='kitchen'),
        ),
    ]
# Generated by Django 4.2.4 on 2023-11-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_purchasedetaile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasedetaile',
            name='username',
        ),
        migrations.AddField(
            model_name='purchasedetaile',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
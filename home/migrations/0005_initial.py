# Generated by Django 4.2.4 on 2023-10-01 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_delete_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('detaile', models.TextField(max_length=1000)),
                ('size', models.CharField(max_length=10)),
                ('catagory', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='home.catagory')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseDetaile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.DecimalField(decimal_places=5, max_digits=10)),
                ('breadth', models.DecimalField(decimal_places=5, max_digits=10)),
                ('area', models.DecimalField(decimal_places=5, max_digits=10)),
                ('address', models.TextField(max_length=2000)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
                ('username', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
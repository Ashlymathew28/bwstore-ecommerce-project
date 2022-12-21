# Generated by Django 4.1.4 on 2022-12-16 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=300)),
                ('category_image', models.ImageField(blank=True, upload_to='assets/images/category')),
            ],
        ),
    ]

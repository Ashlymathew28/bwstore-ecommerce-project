# Generated by Django 4.1.4 on 2022-12-21 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='modifes_date',
            new_name='modified_date',
        ),
    ]
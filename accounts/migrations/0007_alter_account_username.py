# Generated by Django 4.1.4 on 2022-12-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_account_options_remove_account_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-21 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ac_app', '0002_rename_rating_accaunt_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accaunt',
            name='login',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='accaunt',
            name='status',
            field=models.CharField(default='', max_length=70),
        ),
    ]

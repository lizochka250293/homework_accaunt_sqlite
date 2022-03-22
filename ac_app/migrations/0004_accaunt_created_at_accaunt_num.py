# Generated by Django 4.0.3 on 2022-03-21 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ac_app', '0003_alter_accaunt_login_alter_accaunt_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='accaunt',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='accaunt',
            name='num',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]

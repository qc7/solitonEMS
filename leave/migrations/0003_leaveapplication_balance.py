# Generated by Django 2.2.1 on 2019-07-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_leaveapplication_no_of_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplication',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]

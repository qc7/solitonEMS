# Generated by Django 3.0 on 2020-02-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_auto_20200203_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='status',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]

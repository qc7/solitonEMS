# Generated by Django 3.0 on 2020-01-30 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_and_development', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='format',
            new_name='file_format',
        ),
    ]

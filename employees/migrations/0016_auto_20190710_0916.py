# Generated by Django 2.2.1 on 2019-07-10 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0015_auto_20190709_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('positions', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='departments',
            old_name='teams',
            new_name='n_teams',
        ),
        migrations.RemoveField(
            model_name='departments',
            name='code',
        ),
        migrations.AddField(
            model_name='departments',
            name='status',
            field=models.CharField(default='Active', max_length=15),
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('supervisors', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=15)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Departments')),
            ],
        ),
    ]

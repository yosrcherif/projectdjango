# Generated by Django 3.2.3 on 2021-05-31 18:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('descr', models.TextField(blank=True)),
                ('cmpte', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 5, 31, 20, 5, 6, 819228))),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 5, 31, 20, 5, 6, 819228))),
                ('details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='todolist.userdetails')),
                ('todolist', models.ManyToManyField(null=True, to='todolist.todo')),
            ],
        ),
    ]
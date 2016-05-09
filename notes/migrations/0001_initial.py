# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('apply_date', models.DateField()),
                ('apply_user', models.CharField(max_length=30)),
                ('ext_number', models.DecimalField(max_digits=3, decimal_places=0)),
                ('request_descript', models.TextField(max_length=1024)),
                ('treat_descript', models.TextField(max_length=1024, blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('update_user', models.CharField(max_length=30)),
                ('apply_department', models.ForeignKey(to='notes.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Reqlevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Treat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='request_level',
            field=models.ForeignKey(to='notes.Reqlevel'),
        ),
        migrations.AddField(
            model_name='document',
            name='treat_method',
            field=models.ForeignKey(to='notes.Treat'),
        ),
    ]

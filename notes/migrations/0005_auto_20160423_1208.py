# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_document_treat_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatDoc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('treat_descript', models.TextField(max_length=1024, blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('update_user', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='document',
            name='treat_descript',
        ),
        migrations.RemoveField(
            model_name='document',
            name='treat_method',
        ),
        migrations.AlterField(
            model_name='document',
            name='update_user',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='treatdoc',
            name='docs',
            field=models.ForeignKey(to='notes.Document'),
        ),
        migrations.AddField(
            model_name='treatdoc',
            name='treat_method',
            field=models.ForeignKey(to='notes.Treat'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='category',
            field=models.ForeignKey(to='notes.Category', default=datetime.datetime(2016, 4, 22, 22, 17, 55, 19245, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

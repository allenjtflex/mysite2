# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_document_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='treat_method',
        ),
    ]

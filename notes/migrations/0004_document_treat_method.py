# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_remove_document_treat_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='treat_method',
            field=models.ForeignKey(to='notes.Treat', default=1),
            preserve_default=False,
        ),
    ]

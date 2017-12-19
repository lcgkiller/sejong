# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

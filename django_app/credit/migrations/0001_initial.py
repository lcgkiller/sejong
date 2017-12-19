# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('admission_year', models.IntegerField()),
                ('college', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
                ('core_essential', models.IntegerField()),
                ('core_essential_selection', models.IntegerField()),
                ('major_basic', models.IntegerField()),
                ('sum_of_major', models.IntegerField()),
                ('major_required', models.IntegerField()),
                ('major_select', models.IntegerField()),
                ('sum_of_all', models.IntegerField()),
            ],
        ),
    ]

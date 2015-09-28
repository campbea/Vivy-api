# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20150924_1744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'ordering': ['id'], 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together=set([]),
        ),
    ]

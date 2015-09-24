# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]

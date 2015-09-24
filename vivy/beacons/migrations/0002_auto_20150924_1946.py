# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beacons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beacon',
            old_name='beacon_id',
            new_name='beacon_uuid',
        ),
    ]

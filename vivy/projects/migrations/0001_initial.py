# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('headline', models.CharField(max_length=300)),
                ('logo_url', models.URLField(blank=True, default='')),
                ('opportunity', models.TextField(blank=True, default='')),
                ('solution', models.TextField(blank=True, default='')),
                ('technology', models.TextField(blank=True, default='')),
                ('screenshot', django.contrib.postgres.fields.ArrayField(size=5, base_field=models.URLField(blank=True, default=''))),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('staff', models.ManyToManyField(related_name='project_staff', to='employees.Employee')),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ['-added_at'],
                'verbose_name': 'Project',
            },
        ),
    ]

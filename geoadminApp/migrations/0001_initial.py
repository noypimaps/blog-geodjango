# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 04:28
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('feat_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('attributes', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Layers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layername', models.CharField(max_length=255, unique=True)),
                ('author', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='features',
            name='layer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geoadminApp.Layers'),
        ),
    ]

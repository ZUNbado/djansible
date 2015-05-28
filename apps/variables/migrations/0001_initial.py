# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupVariable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupVariableItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('group', models.ForeignKey(to='variables.GroupVariable')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupVariableItemValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_id', models.PositiveIntegerField()),
                ('value', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupVariableValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_id', models.PositiveIntegerField()),
                ('host_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('variable', models.ForeignKey(to='variables.GroupVariable')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SimpleVariable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SimpleVariableValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_id', models.PositiveIntegerField()),
                ('value', models.CharField(max_length=255, null=True, blank=True)),
                ('host_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('variable', models.ForeignKey(to='variables.SimpleVariable')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VariableType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('validator', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='simplevariable',
            name='variabletype',
            field=models.ForeignKey(to='variables.VariableType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupvariableitemvalue',
            name='group',
            field=models.ForeignKey(to='variables.GroupVariableValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupvariableitemvalue',
            name='host_type',
            field=models.ForeignKey(to='contenttypes.ContentType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupvariableitemvalue',
            name='variable',
            field=models.ForeignKey(to='variables.GroupVariableItems'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupvariableitems',
            name='variabletype',
            field=models.ForeignKey(to='variables.VariableType'),
            preserve_default=True,
        ),
    ]

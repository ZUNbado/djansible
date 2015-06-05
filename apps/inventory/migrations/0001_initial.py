# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('var', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('hosts', models.ManyToManyField(to='inventory.Host', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostGroupGroupVarItemValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostGroupGroupVarValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostgroup', models.ForeignKey(to='inventory.HostGroup')),
                ('var', models.ForeignKey(to='var.GroupVariable')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostGroupSimpleVarValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255)),
                ('hostgroup', models.ForeignKey(to='inventory.HostGroup')),
                ('var', models.ForeignKey(to='var.SimpleVariable')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostGroupVarItemValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostGroupVarValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host', models.ForeignKey(to='inventory.Host')),
                ('var', models.ForeignKey(to='var.GroupVariable')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostSimpleVarValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255)),
                ('host', models.ForeignKey(to='inventory.Host')),
                ('var', models.ForeignKey(to='var.SimpleVariable')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='hostgroupvaritemvalue',
            name='group',
            field=models.ForeignKey(to='inventory.HostGroupVarValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hostgroupvaritemvalue',
            name='item',
            field=models.ForeignKey(to='var.GroupVariableItems'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hostgroupgroupvaritemvalue',
            name='group',
            field=models.ForeignKey(to='inventory.HostGroupGroupVarValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hostgroupgroupvaritemvalue',
            name='item',
            field=models.ForeignKey(to='var.GroupVariableItems'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='hostgroups',
            field=models.ManyToManyField(to='inventory.HostGroup', blank=True),
            preserve_default=True,
        ),
    ]

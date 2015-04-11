# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('org_type', models.CharField(max_length=3, choices=[(b'BUS', b'Business'), (b'NPO', b'Non-profit'), (b'GOV', b'Government')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current', models.CharField(max_length=3, choices=[(b'YES', b'Current'), (b'NO', b'Past')])),
                ('role', models.CharField(max_length=1, choices=[(b'B', b'Board Member'), (b'M', b'Management Team'), (b'E', b'Employee')])),
                ('organization', models.ForeignKey(to='boards.Organization')),
                ('person', models.ForeignKey(to='boards.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(to='boards.Person', through='boards.Relationship'),
            preserve_default=True,
        ),
    ]

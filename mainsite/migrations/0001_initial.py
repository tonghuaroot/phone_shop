# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField(default=b'http://i.imgur.com/Ous4iGB.png')),
                ('maker', models.ForeignKey(to='mainsite.Maker')),
            ],
        ),
        migrations.CreateModel(
            name='PPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default=b'\xe4\xba\xa7\xe5\x93\x81\xe7\x85\xa7\xe7\x89\x87', max_length=20)),
                ('url', models.URLField(default=b'http://i.imgur.com/Z230eeq.png')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickename', models.CharField(default=b'\xe8\xb6\x85\xe5\x80\xbc\xe4\xba\x8c\xe6\x89\x8b\xe6\x9c\xba', max_length=15)),
                ('description', models.TextField(default=b'\xe6\x9a\x82\xe6\x97\xa0\xe8\xaf\xb4\xe6\x98\x8e')),
                ('year', models.PositiveIntegerField(default=2017)),
                ('price', models.PositiveIntegerField(default=0)),
                ('pmodel', models.ForeignKey(to='mainsite.PModel')),
            ],
        ),
        migrations.AddField(
            model_name='pphoto',
            name='product',
            field=models.ForeignKey(to='mainsite.Product'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cus_name', models.CharField(max_length=10, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('cus_phone', models.CharField(max_length=11, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe6\x96\xb9\xe5\xbc\x8f')),
                ('cus_mesg', models.CharField(max_length=255, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xbf\xa1\xe6\x81\xaf')),
            ],
        ),
        migrations.CreateModel(
            name='NewsList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('new_content', models.TextField(verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe5\x86\x85\xe5\xae\xb9')),
            ],
        ),
        migrations.CreateModel(
            name='ProList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pro_name', models.CharField(max_length=30, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('pro_img', models.ImageField(upload_to=b'ProIMg/', verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x87')),
            ],
        ),
    ]

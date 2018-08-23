# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club_c', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubuser',
            name='photo',
            field=models.ImageField(default=b'image_head/timg.jpeg', upload_to=b'image_head/'),
        ),
    ]

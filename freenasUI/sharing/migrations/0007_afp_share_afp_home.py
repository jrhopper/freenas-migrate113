# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-27 20:38
from __future__ import unicode_literals

from django.db import migrations, models


def migrate_afp_home(apps, schema_editor):
    AFP = apps.get_model('services', 'afp')
    AFP_Share = apps.get_model('sharing', 'afp_share')
    for service in AFP.objects.all():
        if service.afp_srv_homedir_enable:
            share = AFP_Share()
            share.afp_path = service.afp_srv_homedir
            share.afp_home = True
            share.afp_name = service.afp_srv_homename or "Homes"
            share.afp_timemachine = service.afp_srv_hometimemachine
            share.save()


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('sharing', '0006_afp_share_afp_timemachine_quota_in_gib'),
    ]

    operations = [
        migrations.AddField(
            model_name='afp_share',
            name='afp_home',
            field=models.BooleanField(default=False, verbose_name='Use as home share'),
        ),
        migrations.RunPython(
            migrate_afp_home,
        ),
    ]

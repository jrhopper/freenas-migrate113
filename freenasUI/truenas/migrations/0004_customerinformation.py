# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-20 08:06
from __future__ import unicode_literals

from datetime import datetime

from django.db import migrations, models


def create_customer_information(apps, schema_editor):
    CustomerInformation = apps.get_model("truenas", "CustomerInformation")
    db_alias = schema_editor.connection.alias
    CustomerInformation.objects.using(db_alias).bulk_create([
        CustomerInformation(data="null", updated_at=datetime.min, sent_at=None, form_dismissed=False),
    ])

def delete_customer_information(apps, schema_editor):
    CustomerInformation = apps.get_model("truenas", "CustomerInformation")
    db_alias = schema_editor.connection.alias
    CustomerInformation.objects.using(db_alias).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('truenas', '0003_default_sysctls'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('updated_at', models.DateTimeField()),
                ('sent_at', models.DateTimeField(null=True)),
                ('form_dismissed', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(create_customer_information, delete_customer_information)
    ]

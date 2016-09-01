# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-29 17:10
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mturk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTurkHITType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('string_id', models.CharField(max_length=64, null=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('keywords', models.CharField(blank=True, max_length=128, null=True)),
                ('duration', models.DurationField(null=True)),
                ('boomerang_threshold', models.IntegerField(default=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
                ('status', models.CharField(default='Active', max_length=16)),
                ('auto_granted', models.BooleanField(default=False)),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), default=[], null=True, size=None)),
                ('auto_granted_value', models.IntegerField(default=199, null=True)),
                ('type_id', models.CharField(max_length=128)),
                ('flag', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mturk_qualifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='mturkaccount',
            old_name='created_timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='mturkaccount',
            old_name='last_updated',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='mturkassignment',
            old_name='created_timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='mturkassignment',
            old_name='last_updated',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='mturkhit',
            old_name='created_timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='mturkhit',
            old_name='last_updated',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='mturknotification',
            old_name='created_timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='mturknotification',
            old_name='last_updated',
            new_name='updated_at',
        ),
    ]
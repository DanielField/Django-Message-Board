# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-20 12:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2048)),
                ('likes', models.IntegerField(default=0)),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('isLocked', models.BooleanField(default=False)),
                ('boardId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msgboard.Board')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='msg',
            name='TopicId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msgboard.Topic'),
        ),
        migrations.AddField(
            model_name='msg',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
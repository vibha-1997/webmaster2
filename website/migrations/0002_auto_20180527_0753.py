# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 07:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dimensions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dim_w', models.IntegerField(default=0)),
                ('dim_h', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='room_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=200)),
                ('img_file_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='room_category_size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_width', models.IntegerField(default=0)),
                ('cat_height', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.room_category')),
            ],
        ),
        migrations.AddField(
            model_name='dimensions',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.room_category'),
        ),
        migrations.AddField(
            model_name='dimensions',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.room_category_size'),
        ),
    ]

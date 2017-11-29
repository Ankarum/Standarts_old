# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CommonWorkFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('qualificationLevel', models.IntegerField()),
                ('accessRequirements', models.ManyToManyField(to='Competentions.AccessRequirement')),
            ],
        ),
        migrations.CreateModel(
            name='EducationRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NeccessaryKnowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NeccessarySkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PositionTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Standart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('commonWorkFunction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Competentions.CommonWorkFunction')),
                ('neccessaryKnowledges', models.ManyToManyField(to='Competentions.NeccessaryKnowledge')),
                ('neccessarySkills', models.ManyToManyField(to='Competentions.NeccessarySkill')),
                ('workActions', models.ManyToManyField(to='Competentions.WorkAction')),
            ],
        ),
        migrations.CreateModel(
            name='WorkRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='commonworkfunction',
            name='educationRequirements',
            field=models.ManyToManyField(to='Competentions.EducationRequirement'),
        ),
        migrations.AddField(
            model_name='commonworkfunction',
            name='positionTitles',
            field=models.ManyToManyField(to='Competentions.PositionTitle'),
        ),
        migrations.AddField(
            model_name='commonworkfunction',
            name='standart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Competentions.Standart'),
        ),
        migrations.AddField(
            model_name='commonworkfunction',
            name='workRequirements',
            field=models.ManyToManyField(to='Competentions.WorkRequirement'),
        ),
    ]

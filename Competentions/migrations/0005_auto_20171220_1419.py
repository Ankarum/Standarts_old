# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Competentions', '0004_auto_20171220_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customcompetentionlist',
            name='customCopetentions',
            field=models.ManyToManyField(blank=True, null=True, to='Competentions.CustomCompetention'),
        ),
        migrations.AlterField(
            model_name='customcompetentionlist',
            name='generalProfessionalCompetentions',
            field=models.ManyToManyField(blank=True, null=True, to='Competentions.EducationalStandartCompetention'),
        ),
        migrations.AlterField(
            model_name='customcompetentionlist',
            name='neccessaryKnowledges',
            field=models.ManyToManyField(blank=True, null=True, to='Competentions.NeccessaryKnowledge'),
        ),
        migrations.AlterField(
            model_name='customcompetentionlist',
            name='neccessarySkills',
            field=models.ManyToManyField(blank=True, null=True, to='Competentions.NeccessarySkill'),
        ),
        migrations.AlterField(
            model_name='customcompetentionlist',
            name='workActions',
            field=models.ManyToManyField(blank=True, null=True, to='Competentions.WorkAction'),
        ),
    ]

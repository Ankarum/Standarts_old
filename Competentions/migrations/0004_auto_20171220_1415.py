# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Competentions', '0003_auto_20171220_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customcompetentionlist',
            name='customCopetentions',
            field=models.ManyToManyField(null=True, to='Competentions.CustomCompetention'),
        ),
        migrations.AlterField(
            model_name='customcompetentionlist',
            name='generalProfessionalCompetentions',
            field=models.ManyToManyField(null=True, to='Competentions.EducationalStandartCompetention'),
        ),
    ]

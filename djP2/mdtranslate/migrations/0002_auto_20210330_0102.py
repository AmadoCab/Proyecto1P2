# Generated by Django 3.1.6 on 2021-03-30 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdtranslate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.TextField(default='# <django.db.models.fields.CharField>\n<django.db.models.fields.related.ForeignKey>\n<django.db.models.fields.DateTimeField>\n\n## Introduction\n'),
        ),
    ]
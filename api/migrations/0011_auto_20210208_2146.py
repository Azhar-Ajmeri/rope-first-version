# Generated by Django 3.1.1 on 2021-02-08 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_workpackage_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='subworkpackage',
            name='border_color',
            field=models.CharField(default='#ffffff', max_length=8),
        ),
        migrations.AddField(
            model_name='workpackage',
            name='border_color',
            field=models.CharField(default='#ffffff', max_length=8),
        ),
    ]

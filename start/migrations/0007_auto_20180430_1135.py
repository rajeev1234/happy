# Generated by Django 2.0.3 on 2018-04-30 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0006_auto_20180430_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='updated',
        ),
    ]

# Generated by Django 2.0.3 on 2018-04-28 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0003_auto_20180428_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='ip_address',
            new_name='ip',
        ),
    ]
# Generated by Django 2.0.3 on 2018-04-30 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0011_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='heading',
            new_name='callMe',
        ),
    ]

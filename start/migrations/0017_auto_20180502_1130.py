# Generated by Django 2.0.3 on 2018-05-02 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0016_fileupload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileupload',
            old_name='File',
            new_name='files',
        ),
    ]

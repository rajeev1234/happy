# Generated by Django 2.0.3 on 2018-05-02 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0017_auto_20180502_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileupload',
            old_name='files',
            new_name='file',
        ),
    ]

# Generated by Django 3.2.14 on 2022-11-05 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CreamyBunApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TaskIdToTaskState',
            new_name='KeyToValue',
        ),
        migrations.RenameField(
            model_name='keytovalue',
            old_name='task_id',
            new_name='key',
        ),
        migrations.RenameField(
            model_name='keytovalue',
            old_name='task_state',
            new_name='value',
        ),
    ]
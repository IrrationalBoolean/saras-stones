# Generated by Django 3.2.6 on 2021-08-31 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sarasstones', '0002_auto_20210831_0337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='color',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='cut',
            old_name='cut',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='mineral',
            old_name='mineral',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='stone',
            old_name='stone_color',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='stone',
            old_name='stone_cut',
            new_name='cut',
        ),
        migrations.RenameField(
            model_name='stone',
            old_name='stone_mineral',
            new_name='mineral',
        ),
        migrations.RenameField(
            model_name='stone',
            old_name='stone_name',
            new_name='name',
        ),
    ]
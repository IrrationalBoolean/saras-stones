# Generated by Django 3.2.6 on 2021-08-31 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarasstones', '0004_auto_20210831_0410'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]

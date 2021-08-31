# Generated by Django 3.2.6 on 2021-08-31 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sarasstones', '0005_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_out', models.DateTimeField()),
                ('check_in', models.DateTimeField(blank=True, null=True)),
                ('stone', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sarasstones.stone')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sarasstones.user')),
            ],
        ),
    ]
# Generated by Django 5.2.1 on 2025-05-22 18:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='Balance',
        ),
        migrations.AddField(
            model_name='balance',
            name='wallet',
            field=models.PositiveIntegerField(default=0, verbose_name='balance'),
        ),
        migrations.AlterField(
            model_name='balance',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userbalance', to=settings.AUTH_USER_MODEL),
        ),
    ]

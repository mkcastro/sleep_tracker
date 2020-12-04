# Generated by Django 3.0.11 on 2020-12-04 19:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201205_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='sleep',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sleep',
            name='end_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='end at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sleep',
            name='start_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='start at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sleep',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='created at'),
        ),
    ]

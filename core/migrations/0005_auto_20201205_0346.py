# Generated by Django 3.0.11 on 2020-12-04 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201205_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleep',
            name='bed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Bed', verbose_name='bed'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1 on 2024-08-18 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_region_comuna'),
    ]

    operations = [
        migrations.AddField(
            model_name='vivienda',
            name='comuna',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.comuna'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-12 10:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0023_alter_studentregistrationproxy_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregistration',
            name='admission_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

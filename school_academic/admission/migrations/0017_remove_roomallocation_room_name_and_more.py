# Generated by Django 5.1.2 on 2024-11-05 17:51

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0016_setroom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomallocation',
            name='room_name',
        ),
        migrations.RemoveField(
            model_name='roomallocation',
            name='room_number',
        ),
        migrations.RemoveField(
            model_name='roomallocation',
            name='student_name',
        ),
        migrations.AddField(
            model_name='roomallocation',
            name='allocated_dormitory',
            field=models.ForeignKey(default='a', on_delete=django.db.models.deletion.CASCADE, to='admission.setroom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roomallocation',
            name='allocation_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roomallocation',
            name='student',
            field=models.ForeignKey(default='student', on_delete=django.db.models.deletion.CASCADE, to='admission.studentregistration'),
            preserve_default=False,
        ),
    ]
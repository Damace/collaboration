# Generated by Django 5.1.2 on 2024-11-02 08:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_setting', '0012_alter_class_programme'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='publish',
            name='published_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publish',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publish',
            name='action',
            field=models.CharField(choices=[('published', 'Published'), ('unpublished', 'Unpublished')], default='unpublish', max_length=20),
        ),
    ]
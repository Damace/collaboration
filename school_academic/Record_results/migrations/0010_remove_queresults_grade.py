# Generated by Django 5.1.2 on 2024-11-06 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Record_results', '0009_queresults_programme_queresults_stream_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queresults',
            name='grade',
        ),
    ]

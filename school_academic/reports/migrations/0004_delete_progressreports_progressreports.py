# Generated by Django 5.1.2 on 2024-11-11 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0023_alter_studentregistrationproxy_options'),
        ('reports', '0003_studentassessment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProgressReports',
        ),
        migrations.CreateModel(
            name='ProgressReports',
            fields=[
            ],
            options={
                'verbose_name': 'Progress report',
                'verbose_name_plural': 'Progress report',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('admission.studentregistration',),
        ),
    ]

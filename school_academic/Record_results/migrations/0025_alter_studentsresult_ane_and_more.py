# Generated by Django 5.1.2 on 2024-11-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Record_results', '0024_alter_studentsassasmentsproxy_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsresult',
            name='ane',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentsresult',
            name='average',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentsresult',
            name='mte',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentsresult',
            name='mtt1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentsresult',
            name='mtt2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentsresult',
            name='te',
            field=models.CharField(max_length=100),
        ),
    ]

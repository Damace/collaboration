# Generated by Django 5.1.2 on 2024-11-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Record_results', '0031_alter_studentsresult_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsresult',
            name='position',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-10 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Record_results', '0010_remove_queresults_grade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='queresults',
            options={'verbose_name': 'Que Results', 'verbose_name_plural': 'Que Results'},
        ),
        migrations.AddField(
            model_name='queresults',
            name='exam_type',
            field=models.CharField(default='quiz', editable=False, max_length=100),
            preserve_default=False,
        ),
    ]

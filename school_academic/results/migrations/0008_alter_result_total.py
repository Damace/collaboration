# Generated by Django 5.1.2 on 2024-11-03 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0007_alter_result_academic_year_alter_result_class_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
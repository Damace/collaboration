# Generated by Django 5.1.2 on 2024-11-04 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0012_delete_examinationresults'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
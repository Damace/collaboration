# Generated by Django 5.1.2 on 2024-10-25 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('subjects_count', models.PositiveIntegerField()),
            ],
        ),
    ]
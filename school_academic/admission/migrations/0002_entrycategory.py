# Generated by Django 5.1.2 on 2024-10-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_category', models.CharField(max_length=255)),
            ],
        ),
    ]

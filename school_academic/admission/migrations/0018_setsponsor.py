# Generated by Django 5.1.2 on 2024-11-05 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0017_remove_roomallocation_room_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_name', models.CharField(max_length=255)),
            ],
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-29 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0026_remove_sponsor_email_remove_sponsor_mobile_and_more'),
        ('main_setting', '0019_delete_studentsresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistration',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='StudentRegistration', to='main_setting.subject'),
        ),
    ]

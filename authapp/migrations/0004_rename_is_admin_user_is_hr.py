# Generated by Django 3.2.25 on 2024-05-30 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_hr',
        ),
    ]

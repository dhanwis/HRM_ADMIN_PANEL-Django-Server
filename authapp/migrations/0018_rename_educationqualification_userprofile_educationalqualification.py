# Generated by Django 4.1 on 2024-07-24 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0017_rename_degree_program_userprofile_educationqualification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='educationqualification',
            new_name='educationalQualification',
        ),
    ]

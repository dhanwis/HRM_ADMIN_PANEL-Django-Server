# Generated by Django 4.1 on 2024-07-19 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0043_alter_machineallocate_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapply',
            old_name='mode_of_work',
            new_name='status',
        ),
    ]

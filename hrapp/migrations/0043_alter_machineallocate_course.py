# Generated by Django 4.2.10 on 2024-07-01 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0014_alter_userprofile_degree_program'),
        ('hrapp', '0042_machineallocate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machineallocate',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allocated_courses', to='authapp.userprofile', to_field='degree_program'),
        ),
    ]

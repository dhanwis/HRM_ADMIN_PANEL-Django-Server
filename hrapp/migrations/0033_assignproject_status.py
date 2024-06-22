# Generated by Django 5.0.6 on 2024-06-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0032_studentassign_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignproject',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In progress', 'In progress'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]

# Generated by Django 3.2.25 on 2024-06-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0012_delete_leaveform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('duration_days', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'pending'), ('Approve', 'Approve'), ('Reject', 'Reject')], default='pending', max_length=10)),
            ],
        ),
    ]
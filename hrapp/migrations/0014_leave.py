# Generated by Django 4.2.10 on 2024-06-08 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0013_alter_studentassign_guide_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('duration_days', models.IntegerField(editable=False)),
            ],
        ),
    ]

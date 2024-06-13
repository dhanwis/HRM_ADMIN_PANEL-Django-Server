# Generated by Django 3.2.25 on 2024-06-06 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_rename_is_admin_user_is_hr'),
        ('hrapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAssign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(blank=True, max_length=100, null=True)),
                ('task_details', models.CharField(blank=True, max_length=100, null=True)),
                ('guide_name', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('student_name', models.ForeignKey(limit_choices_to={'is_intern': True}, on_delete=django.db.models.deletion.CASCADE, to='authapp.user')),
            ],
        ),
    ]

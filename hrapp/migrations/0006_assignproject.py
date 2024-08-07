# Generated by Django 4.2.10 on 2024-06-06 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hrapp', '0005_studentassign'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(blank=True, max_length=100)),
                ('projectdate', models.DateField()),
                ('deadline', models.DateField()),
                ('employeename', models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

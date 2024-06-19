# Generated by Django 4.2.10 on 2024-06-06 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hrapp', '0007_alter_assignproject_employeename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentassign',
            name='guide_name',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AlterField(
            model_name='studentassign',
            name='student_name',
            field=models.ForeignKey(limit_choices_to={'is_intern': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
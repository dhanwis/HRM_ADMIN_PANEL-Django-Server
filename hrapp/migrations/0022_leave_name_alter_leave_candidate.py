# Generated by Django 4.2.10 on 2024-06-15 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hrapp', '0021_alter_leave_candidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='name',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='leave',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leave_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]

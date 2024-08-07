# Generated by Django 3.2.25 on 2024-05-15 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20240515_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=100)),
                ('degree_program', models.CharField(max_length=100)),
                ('internship_position', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('intership_type', models.CharField(max_length=50)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stipend_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authapp.user')),
            ],
        ),
    ]

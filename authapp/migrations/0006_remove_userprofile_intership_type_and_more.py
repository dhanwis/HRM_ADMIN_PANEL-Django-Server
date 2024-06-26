# Generated by Django 5.0.6 on 2024-06-18 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_remove_user_is_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='intership_type',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='paid_amount',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='stipend_amount',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='category',
            field=models.CharField(choices=[('Student', 'Student'), ('Product', 'Product')], default=1, max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='no_of_installments',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='payment',
            field=models.CharField(choices=[('Total Amount', 'Total Amount'), ('Installment', 'Installment')], default=1, max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='payment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

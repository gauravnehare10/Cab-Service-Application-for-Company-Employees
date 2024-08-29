# Generated by Django 5.0.6 on 2024-08-28 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabservice', '0002_alter_employee_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('pickup_slot', models.CharField(choices=[('7:00 AM - 8:00 AM', '7:00 AM - 8:00 AM'), ('8:00 AM - 9:00 AM', '8:00 AM - 9:00 AM'), ('9:00 AM - 10:00 AM', '9:00 AM - 10:00 AM'), ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM')], max_length=20)),
                ('return_slot', models.CharField(choices=[('4:00 PM - 5:00 PM', '4:00 PM - 5:00 PM'), ('5:00 PM - 6:00 PM', '5:00 PM - 6:00 PM'), ('6:00 PM - 7:00 PM', '6:00 PM - 7:00 PM'), ('7:00 PM - 8:00 PM', '7:00 PM - 8:00 PM')], max_length=20)),
                ('pickup_location', models.CharField(max_length=255)),
                ('dropoff_location', models.CharField(editable=False, max_length=255)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled'), ('completed', 'Completed')], default='pending', max_length=10)),
                ('cab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabservice.cabinfo')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabservice.employee')),
            ],
        ),
    ]
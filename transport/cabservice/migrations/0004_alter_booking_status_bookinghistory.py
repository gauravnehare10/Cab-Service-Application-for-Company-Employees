# Generated by Django 5.0.6 on 2024-09-28 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabservice', '0003_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], default='pending', max_length=10),
        ),
        migrations.CreateModel(
            name='BookingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('pickup_slot', models.CharField(max_length=20)),
                ('return_slot', models.CharField(max_length=20)),
                ('pickup_location', models.CharField(max_length=255)),
                ('dropoff_location', models.CharField(editable=False, max_length=255)),
                ('status', models.CharField(max_length=10)),
                ('cab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabservice.cabinfo')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabservice.employee')),
            ],
        ),
    ]

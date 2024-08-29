from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_default_user():
    return User.objects.first()

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    employee_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id})"
    
class CabInfo(models.Model):
    cab_number = models.CharField(max_length=15, unique=True)
    model = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    driver_name = models.CharField(max_length=100)
    driver_phone = models.CharField(max_length=15)
    availability_status_choices = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('in_maintenance', 'In Maintenance'),
    ]
    availability_status = models.CharField(max_length=15, choices=availability_status_choices, default='available')

    def __str__(self):
        return f"{self.model} ({self.cab_number}) - Driver: {self.driver_name}"

class Booking(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    cab = models.ForeignKey(CabInfo, on_delete=models.SET_NULL, null=True, blank=True)
    booking_date = models.DateField(auto_now_add=True)
    
    PICKUP_SLOT_CHOICES = [
        ('7:00 AM - 8:00 AM', '7:00 AM - 8:00 AM'),
        ('8:00 AM - 9:00 AM', '8:00 AM - 9:00 AM'),
        ('9:00 AM - 10:00 AM', '9:00 AM - 10:00 AM'),
        ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM'),
    ]
    RETURN_SLOT_CHOICES = [
        ('4:00 PM - 5:00 PM', '4:00 PM - 5:00 PM'),
        ('5:00 PM - 6:00 PM', '5:00 PM - 6:00 PM'),
        ('6:00 PM - 7:00 PM', '6:00 PM - 7:00 PM'),
        ('7:00 PM - 8:00 PM', '7:00 PM - 8:00 PM'),
    ]
    
    pickup_slot = models.CharField(max_length=20, choices=PICKUP_SLOT_CHOICES)
    return_slot = models.CharField(max_length=20, choices=RETURN_SLOT_CHOICES)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255, editable=False)
    status_choices = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    def save(self, *args, **kwargs):
        self.dropoff_location = self.employee.address
        self.pickup_location = self.employee.address
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f"Booking by {self.employee} on {self.booking_date} - Status: {self.status}"

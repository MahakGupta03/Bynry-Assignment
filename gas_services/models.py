from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    account_number = models.CharField(max_length=20, unique=True)
    meter_number = models.CharField(max_length=20)
    
class ServiceRequest(models.Model):
    REQUEST_TYPES = (
        ('LEAK', 'Gas Leak'),
        ('METER', 'Meter Issue'),
        ('BILL', 'Billing'),
        ('OTHER', 'Other'),
    )
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    submitted_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(null=True, blank=True)
    # resolved_date = models.DateTimeField(auto_now =True)
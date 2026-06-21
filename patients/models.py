from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    blood_group_choices = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    blood_group = models.CharField(max_length=3, choices=blood_group_choices)
    problems = models.TextField()
   
    def __str__(self):
        return self.name    
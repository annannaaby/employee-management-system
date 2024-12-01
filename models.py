from django.db import models

# Create your models here.

class DynamicField(models.Model):
    FIELD_TYPES = [
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('password', 'Password'),
    ]
    label = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20, choices=FIELD_TYPES)

class Employee(models.Model):
    name = models.CharField(max_length=255)
    dynamic_data = models.JSONField()

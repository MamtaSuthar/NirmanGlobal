from django.db import models

class DesignBooking(models.Model):
    SERVICE_CHOICES = [
        ('3D', '3D Design'),
        ('4D', '4D Design'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service_type = models.CharField(max_length=2, choices=SERVICE_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service_type}"
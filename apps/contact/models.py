from django.db import models

class Contact(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General Inquiry'),
        ('pricing', 'Pricing'),
        ('design', 'Custom Fabrication'),
        ('complaint', 'Complaint'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    is_read = models.BooleanField(default=False)  # admin usage
    ai_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)

    image = models.ImageField(upload_to='testimonials/')

    message = models.TextField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
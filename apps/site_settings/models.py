from django.db import models

class SiteSettings(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    def __str__(self):
        return "Site Settings"
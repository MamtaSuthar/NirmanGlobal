from django.db import models

class SiteSettings(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram_qr = models.ImageField(
        upload_to='site/qr/',
        blank=True,
        null=True,
        help_text="QR code image linking to the company Instagram profile"
    )

    def __str__(self):
        return "Site Settings"
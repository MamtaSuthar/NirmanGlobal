from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="Use class like flaticon-bedroom")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="service_images/")

    def __str__(self):
        return f"{self.service.title} image"
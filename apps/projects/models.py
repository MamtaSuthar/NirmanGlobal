from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):

    STATUS_CHOICES = (
        ('complete', 'Complete'),
        ('running', 'Running'),
        ('upcoming', 'Upcoming'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='complete'
    )

    location = models.CharField(max_length=150, blank=True)
    description = models.TextField()

    cover_image = models.ImageField(upload_to='projects/covers/')

    budget_range = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: 5–10 Lakhs"
    )

    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # ✅ for hiding projects

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(upload_to='projects/gallery/')

    is_before = models.BooleanField(
        default=False,
        help_text="Check if this is a BEFORE image"
    )

    def __str__(self):
        return f"{self.project.title} Image"
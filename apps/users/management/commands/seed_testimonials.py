from django.core.management.base import BaseCommand
from django.core.files import File
from apps.testimonials.models import Testimonial
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Seed testimonials'

    def handle(self, *args, **kwargs):

        data = [
            ("Rahul Sharma", "Business Owner", "testimonial-1.jpg"),
            ("Priya Mehta", "Architect", "testimonial-2.jpg"),
        ]

        for name, profession, image_name in data:
            obj, created = Testimonial.objects.get_or_create(
                name=name,
                defaults={
                    "profession": profession,
                    "message": "Amazing service! Highly recommended.",
                    "is_active": True
                }
            )

            if created:
                image_path = os.path.join(settings.BASE_DIR, 'static/img', image_name)
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as f:
                        obj.image.save(image_name, File(f), save=True)

        self.stdout.write(self.style.SUCCESS("✅ Testimonials seeded"))
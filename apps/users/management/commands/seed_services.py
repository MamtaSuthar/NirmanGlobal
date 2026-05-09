from django.core.management.base import BaseCommand
from apps.services.models import Service

class Command(BaseCommand):
    help = 'Seed dummy services data'

    def handle(self, *args, **kwargs):

        services_data = [
            {
                "title": "Bedroom Design",
                "description": "Modern and stylish bedroom interiors.",
                "icon": "flaticon-bedroom"
            },
            {
                "title": "Kitchen Design",
                "description": "Smart and modular kitchen layouts.",
                "icon": "flaticon-kitchen"
            },
            {
                "title": "Bathroom Design",
                "description": "Luxury and elegant bathroom spaces.",
                "icon": "flaticon-bathroom"
            },
        ]

        for service in services_data:
            if not Service.objects.filter(title=service["title"]).exists():
                Service.objects.create(**service)

        self.stdout.write(self.style.SUCCESS('Services seeded successfully'))
from django.core.management.base import BaseCommand
from apps.projects.models import Category, Project

class Command(BaseCommand):
    help = "Seed project data"

    def handle(self, *args, **kwargs):

        # Create categories (based on your filter UI)
        complete_cat, _ = Category.objects.get_or_create(
            name="Complete", slug="complete"
        )
        running_cat, _ = Category.objects.get_or_create(
            name="Running", slug="running"
        )
        upcoming_cat, _ = Category.objects.get_or_create(
            name="Upcoming", slug="upcoming"
        )

        projects_data = [
            ("Modern Living Room", complete_cat, "projects/covers/portfolio-1.jpg", "complete"),
            ("Luxury Apartment", running_cat, "projects/covers/portfolio-2.jpg", "running"),
            ("Minimal Interior", upcoming_cat, "projects/covers/portfolio-3.jpg", "upcoming"),
            ("Office Workspace", complete_cat, "projects/covers/portfolio-4.jpg", "complete"),
            ("Kitchen Design", running_cat, "projects/covers/portfolio-5.jpg", "running"),
            ("Bedroom Setup", upcoming_cat, "projects/covers/portfolio-6.jpg", "upcoming"),
        ]

        for title, category, image, status in projects_data:
            Project.objects.get_or_create(
                title=title,
                defaults={
                    "category": category,
                    "status": status,
                    "description": f"{title} description",
                    "cover_image": image,
                    "is_featured": True,
                }
            )

        self.stdout.write(self.style.SUCCESS("✅ Projects Seeded Successfully"))
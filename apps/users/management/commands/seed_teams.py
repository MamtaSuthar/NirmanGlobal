from django.core.management.base import BaseCommand
from django.core.files import File
from apps.team.models import TeamMember
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Seed team data'

    def handle(self, *args, **kwargs):

        team_data = [
            ("John Doe", "Interior Designer", "team-1.jpg"),
            ("Jane Smith", "Architect", "team-2.jpg"),
            ("Mike Johnson", "Project Manager", "team-3.jpg"),
            ("Sara Khan", "UI Designer", "team-4.jpg"),
        ]

        for name, designation, image_name in team_data:

            member, created = TeamMember.objects.get_or_create(
                name=name,
                defaults={
                    "designation": designation,
                    "is_active": True
                }
            )

            if created:
                image_path = os.path.join(settings.BASE_DIR, 'static/img', image_name)

                if os.path.exists(image_path):
                    with open(image_path, 'rb') as f:
                        member.image.save(image_name, File(f), save=True)

        self.stdout.write(self.style.SUCCESS("✅ Team members seeded successfully"))
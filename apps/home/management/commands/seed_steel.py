"""
Management command to seed steel & aluminium demo data.

Usage:
    python manage.py seed_steel           # seed everything (skips if data exists)
    python manage.py seed_steel --flush   # wipe existing data then re-seed
"""

import io
import os
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.conf import settings


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _placeholder_image(width=400, height=300, color=(45, 55, 72), text=""):
    """
    Generate a minimal PNG placeholder using Pillow.
    Returns a ContentFile ready to assign to an ImageField.
    """
    from PIL import Image, ImageDraw, ImageFont

    img = Image.new("RGB", (width, height), color=color)
    draw = ImageDraw.Draw(img)

    if text:
        # Draw centred text (no external font needed)
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except Exception:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text(
            ((width - tw) // 2, (height - th) // 2),
            text,
            fill=(232, 119, 34),
            font=font,
        )

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return ContentFile(buf.read())


# ---------------------------------------------------------------------------
# Seed data definitions
# ---------------------------------------------------------------------------

SITE_SETTINGS = {
    "email": "info@nirmanglobal.com",
    "phone": "+91 98765 43210",
    "address": "Plot No. 12, Industrial Area, Phase 2, Ahmedabad, Gujarat - 382415",
    "instagram": "https://instagram.com/nirmanglobal",
    "twitter": "https://twitter.com/nirmanglobal",
    "facebook": "https://facebook.com/nirmanglobal",
}

SERVICES = [
    {
        "title": "Aluminium Windows & Doors",
        "icon": "fa fa-window-maximize",
        "description": (
            "We manufacture and install premium aluminium windows and doors for "
            "residential and commercial buildings. Our products offer excellent "
            "thermal insulation, weather resistance, and a sleek modern finish. "
            "Available in sliding, casement, tilt-and-turn, and fixed configurations."
        ),
    },
    {
        "title": "Sliding & Folding Systems",
        "icon": "fa fa-arrows-alt-h",
        "description": (
            "Our sliding and folding door systems are engineered for smooth operation "
            "and long-term durability. Ideal for balconies, patios, and large openings, "
            "they combine functionality with contemporary aesthetics. Custom sizes and "
            "powder-coat finishes available."
        ),
    },
    {
        "title": "Glass Partitions & Facades",
        "icon": "fa fa-border-all",
        "description": (
            "Transform your interior and exterior spaces with our frameless and "
            "semi-framed glass partition systems. Perfect for offices, showrooms, "
            "and commercial lobbies. We use toughened and laminated safety glass "
            "with aluminium or steel framing."
        ),
    },
    {
        "title": "Steel Fabrication",
        "icon": "fa fa-cogs",
        "description": (
            "Custom steel fabrication for structural and architectural applications. "
            "We handle everything from mild steel gates and grilles to heavy structural "
            "frames and staircases. All work is done in-house with precision CNC cutting "
            "and MIG/TIG welding."
        ),
    },
    {
        "title": "Aluminium Cladding",
        "icon": "fa fa-layer-group",
        "description": (
            "Enhance your building's exterior with our aluminium composite panel (ACP) "
            "cladding solutions. We offer a wide range of colours and textures, providing "
            "weather protection, thermal insulation, and a modern architectural look for "
            "both new builds and refurbishments."
        ),
    },
    {
        "title": "Structural Steel Works",
        "icon": "fa fa-industry",
        "description": (
            "End-to-end structural steel solutions including design, fabrication, and "
            "erection. We serve industrial sheds, warehouses, mezzanine floors, and "
            "commercial structures. Our team ensures compliance with IS standards and "
            "delivers projects on schedule."
        ),
    },
]

CATEGORIES = [
    {"name": "Aluminium Works", "slug": "aluminium-works"},
    {"name": "Steel Fabrication", "slug": "steel-fabrication"},
    {"name": "Glass & Glazing",  "slug": "glass-glazing"},
    {"name": "Structural Works", "slug": "structural-works"},
]

PROJECTS = [
    {
        "title": "Commercial Tower Facade — Ahmedabad",
        "category_slug": "aluminium-works",
        "status": "complete",
        "location": "Ahmedabad, Gujarat",
        "description": (
            "Full aluminium composite panel cladding and curtain wall glazing for a "
            "12-storey commercial tower. The project involved 4,200 sqm of ACP cladding, "
            "custom aluminium window frames, and structural silicone glazing. Completed "
            "in 8 months with zero safety incidents."
        ),
        "budget_range": "80–120 Lakhs",
        "is_featured": True,
        "color": (30, 60, 90),
    },
    {
        "title": "Industrial Warehouse Steel Structure",
        "category_slug": "structural-works",
        "status": "complete",
        "location": "Sanand, Gujarat",
        "description": (
            "Design and erection of a 5,000 sqm pre-engineered steel structure for a "
            "manufacturing warehouse. Includes portal frames, roof purlins, side cladding, "
            "and mezzanine floor. Delivered 2 weeks ahead of schedule."
        ),
        "budget_range": "150–200 Lakhs",
        "is_featured": True,
        "color": (50, 50, 50),
    },
    {
        "title": "Luxury Villa Sliding Doors",
        "category_slug": "aluminium-works",
        "status": "complete",
        "location": "Gandhinagar, Gujarat",
        "description": (
            "Supply and installation of large-format aluminium sliding and folding door "
            "systems for a luxury residential villa. 14 openings with double-glazed units, "
            "powder-coated in RAL 7016 anthracite grey. Integrated fly-screen systems included."
        ),
        "budget_range": "12–18 Lakhs",
        "is_featured": True,
        "color": (70, 90, 110),
    },
    {
        "title": "Office Glass Partition System",
        "category_slug": "glass-glazing",
        "status": "complete",
        "location": "Surat, Gujarat",
        "description": (
            "Frameless glass partition system for a 3-floor corporate office. "
            "Used 12mm toughened glass with aluminium top and bottom channels. "
            "Includes 8 swing doors and 2 sliding doors. Total area: 620 sqm."
        ),
        "budget_range": "20–30 Lakhs",
        "is_featured": False,
        "color": (100, 130, 160),
    },
    {
        "title": "Steel Gates & Grilles — Residential Complex",
        "category_slug": "steel-fabrication",
        "status": "complete",
        "location": "Vadodara, Gujarat",
        "description": (
            "Custom fabrication and installation of MS gates, window grilles, and "
            "compound fencing for a 200-unit residential complex. All items hot-dip "
            "galvanised and powder-coated for long-term corrosion resistance."
        ),
        "budget_range": "25–35 Lakhs",
        "is_featured": False,
        "color": (60, 40, 30),
    },
    {
        "title": "Airport Terminal Canopy Structure",
        "category_slug": "structural-works",
        "status": "running",
        "location": "Rajkot, Gujarat",
        "description": (
            "Ongoing fabrication and erection of a 1,200 sqm steel and aluminium canopy "
            "structure for a regional airport terminal entrance. The design features "
            "curved steel arches with polycarbonate roofing and LED-integrated aluminium "
            "fascia panels."
        ),
        "budget_range": "60–90 Lakhs",
        "is_featured": True,
        "color": (20, 40, 70),
    },
]

TEAM = [
    {
        "name": "Rajesh Patel",
        "designation": "Managing Director",
        "twitter": "https://twitter.com/",
        "facebook": "https://facebook.com/",
        "linkedin": "https://linkedin.com/",
        "color": (45, 55, 72),
    },
    {
        "name": "Amit Shah",
        "designation": "Head of Fabrication",
        "twitter": "",
        "facebook": "https://facebook.com/",
        "linkedin": "https://linkedin.com/",
        "color": (60, 70, 85),
    },
    {
        "name": "Priya Mehta",
        "designation": "Project Manager",
        "twitter": "https://twitter.com/",
        "facebook": "",
        "linkedin": "https://linkedin.com/",
        "color": (80, 55, 60),
    },
    {
        "name": "Suresh Kumar",
        "designation": "Senior Structural Engineer",
        "twitter": "",
        "facebook": "https://facebook.com/",
        "linkedin": "https://linkedin.com/",
        "color": (40, 70, 55),
    },
]

TESTIMONIALS = [
    {
        "name": "Vikram Desai",
        "profession": "Real Estate Developer",
        "message": (
            "Nirman Global delivered exceptional aluminium facade work for our commercial "
            "tower. The quality of materials and the precision of installation were "
            "outstanding. They finished ahead of schedule and within budget. Highly recommended."
        ),
        "color": (45, 55, 72),
    },
    {
        "name": "Meena Joshi",
        "profession": "Interior Architect",
        "message": (
            "We've worked with Nirman Global on multiple office fit-out projects. Their "
            "glass partition systems are top-notch and the team is very professional. "
            "They understand design requirements and execute them perfectly."
        ),
        "color": (80, 55, 60),
    },
    {
        "name": "Harish Nair",
        "profession": "Factory Owner",
        "message": (
            "The structural steel warehouse they built for us is solid and well-engineered. "
            "The project was completed 2 weeks early. Communication throughout was excellent "
            "and the pricing was very competitive for the quality delivered."
        ),
        "color": (40, 70, 55),
    },
    {
        "name": "Sunita Agarwal",
        "profession": "Homeowner",
        "message": (
            "Got aluminium sliding doors and windows installed for my villa. The finish is "
            "beautiful and the thermal insulation is noticeably better than my old frames. "
            "The installation team was clean, punctual, and professional."
        ),
        "color": (60, 50, 80),
    },
]


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = "Seed steel & aluminium demo data (services, projects, team, testimonials, site settings)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete existing seed data before re-seeding",
        )

    def handle(self, *args, **options):
        from apps.services.models import Service
        from apps.projects.models import Category, Project
        from apps.team.models import TeamMember
        from apps.testimonials.models import Testimonial
        from apps.site_settings.models import SiteSettings

        flush = options["flush"]

        if flush:
            self.stdout.write(self.style.WARNING("Flushing existing data..."))
            Service.objects.all().delete()
            Category.objects.all().delete()
            Project.objects.all().delete()
            TeamMember.objects.all().delete()
            Testimonial.objects.all().delete()
            SiteSettings.objects.all().delete()
            self.stdout.write(self.style.WARNING("Done flushing.\n"))

        # ── Site Settings ──────────────────────────────────────────────────
        if not SiteSettings.objects.exists():
            SiteSettings.objects.create(**SITE_SETTINGS)
            self.stdout.write(self.style.SUCCESS("✔ Site settings created"))
        else:
            self.stdout.write("  Site settings already exist — skipped")

        # ── Services ───────────────────────────────────────────────────────
        created_services = 0
        for svc in SERVICES:
            if not Service.objects.filter(title=svc["title"]).exists():
                Service.objects.create(
                    title=svc["title"],
                    description=svc["description"],
                    icon=svc["icon"],
                )
                created_services += 1
        self.stdout.write(self.style.SUCCESS(f"✔ Services: {created_services} created"))

        # ── Project Categories ─────────────────────────────────────────────
        created_cats = 0
        for cat in CATEGORIES:
            obj, created = Category.objects.get_or_create(
                slug=cat["slug"],
                defaults={"name": cat["name"]},
            )
            if created:
                created_cats += 1
        self.stdout.write(self.style.SUCCESS(f"✔ Categories: {created_cats} created"))

        # ── Projects ───────────────────────────────────────────────────────
        created_projects = 0
        for proj in PROJECTS:
            if Project.objects.filter(title=proj["title"]).exists():
                continue
            try:
                category = Category.objects.get(slug=proj["category_slug"])
            except Category.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"  Category '{proj['category_slug']}' not found, skipping project"))
                continue

            p = Project(
                title=proj["title"],
                category=category,
                status=proj["status"],
                location=proj["location"],
                description=proj["description"],
                budget_range=proj["budget_range"],
                is_featured=proj["is_featured"],
                is_active=True,
            )
            # Generate placeholder cover image
            img_content = _placeholder_image(800, 500, proj["color"], proj["title"][:30])
            filename = proj["title"].lower().replace(" ", "_").replace(",", "")[:40] + ".png"
            p.cover_image.save(filename, img_content, save=False)
            p.save()
            created_projects += 1

        self.stdout.write(self.style.SUCCESS(f"✔ Projects: {created_projects} created"))

        # ── Team Members ───────────────────────────────────────────────────
        created_team = 0
        for member in TEAM:
            if TeamMember.objects.filter(name=member["name"]).exists():
                continue
            m = TeamMember(
                name=member["name"],
                designation=member["designation"],
                twitter=member["twitter"],
                facebook=member["facebook"],
                linkedin=member["linkedin"],
                is_active=True,
            )
            img_content = _placeholder_image(300, 300, member["color"], member["name"])
            filename = member["name"].lower().replace(" ", "_") + ".png"
            m.image.save(filename, img_content, save=False)
            m.save()
            created_team += 1

        self.stdout.write(self.style.SUCCESS(f"✔ Team members: {created_team} created"))

        # ── Testimonials ───────────────────────────────────────────────────
        created_testimonials = 0
        for t in TESTIMONIALS:
            if Testimonial.objects.filter(name=t["name"]).exists():
                continue
            obj = Testimonial(
                name=t["name"],
                profession=t["profession"],
                message=t["message"],
                is_active=True,
            )
            img_content = _placeholder_image(200, 200, t["color"], t["name"])
            filename = t["name"].lower().replace(" ", "_") + "_testimonial.png"
            obj.image.save(filename, img_content, save=False)
            obj.save()
            created_testimonials += 1

        self.stdout.write(self.style.SUCCESS(f"✔ Testimonials: {created_testimonials} created"))

        self.stdout.write("\n" + self.style.SUCCESS("✅ Seeding complete!"))

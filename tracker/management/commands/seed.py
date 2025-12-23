import random
from datetime import date
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tracker.models import (
    Game, Edition, Platform, Status,
    Medium, SubscriptionService, Library
)

class Command(BaseCommand):
    help = "Seed the database with test data for development"

    def handle(self, *args, **options):
        self.stdout.write("Seeding database...")

        # --- USER ---
        if not User.objects.exists():
            user = User.objects.create_user(
                username="martyn",
                password="password123",
                email="martyn@example.com"
            )
            self.stdout.write("Created default user: martyn / password123")
        else:
            user = User.objects.first()

        # --- STATUSES ---
        statuses = [
            ("wishlist", "Wishlist"),
            ("backlog", "Backlog"),
            ("paused", "Paused"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
            ("shelved", "Shelved"),
            ("abandoned", "Abandoned"),
        ]
        status_objs = []
        for key, label in statuses:
            obj, _ = Status.objects.get_or_create(key=key, label=label)
            status_objs.append(obj)

        # --- PLATFORMS ---
        platforms = [
            ("PC", "Various", "PC"),
            ("PS5", "Sony", "Console"),
            ("Xbox Series", "Microsoft", "Console"),
            ("Switch", "Nintendo", "Console"),
            ("Steam", "Valve", "Service"),
            ("GOG", "CD Projekt", "Service"),
            ("Epic", "Epic Games", "Service"),
        ]
        platform_objs = []
        for name, manufacturer, type in platforms:
            obj, _ = Platform.objects.get_or_create(
                name=name, manufacturer=manufacturer, type=type
            )
            platform_objs.append(obj)

        # --- MEDIUMS ---
        mediums = ["Digital", "Physical", "Cloud", "Subscription", "Emulated"]
        medium_objs = []
        for name in mediums:
            obj, _ = Medium.objects.get_or_create(name=name)
            medium_objs.append(obj)

        # --- SUBSCRIPTION SERVICES ---
        services = ["Game Pass", "PS Plus", "Nintendo Online", "EA Play", "Ubisoft+"]
        service_objs = []
        for name in services:
            obj, _ = SubscriptionService.objects.get_or_create(name=name)
            service_objs.append(obj)

        # --- GAMES + EDITIONS ---
        game_titles = [
            "Elden Ring", "Baldur's Gate 3", "Hades II", "Cyberpunk 2077",
            "The Witcher 3", "Stardew Valley", "Hollow Knight",
            "God of War Ragnarok", "Starfield", "Alan Wake 2",
            "Persona 5 Royal", "Death Stranding", "Returnal",
            "Ghost of Tsushima", "Bloodborne", "Dark Souls III",
            "Final Fantasy VII Remake", "Monster Hunter World",
            "Sekiro", "Control"
        ]

        edition_objs = []

        for title in game_titles:
            game, _ = Game.objects.get_or_create(
                title=title,
                defaults={
                    "release_year": random.randint(2000, 2024),
                    "developer": "",
                    "publisher": "",
                }
            )

            # Create 1–2 editions per game
            for edition_name in ["Standard Edition", "Deluxe Edition"][:random.randint(1, 2)]:
                edition, _ = Edition.objects.get_or_create(
                    game=game,
                    name=edition_name,
                    defaults={
                        "region": random.choice(["EU", "US", "JP", "Global"]),
                        "release_date": date(
                            random.randint(2000, 2024),
                            random.randint(1, 12),
                            random.randint(1, 28)
                        ),
                    }
                )
                # Assign platforms to edition
                edition.platforms.set(random.sample(platform_objs, random.randint(1, 2)))
                edition_objs.append(edition)

        # --- LIBRARY ENTRIES ---
        for edition in edition_objs:
            Library.objects.get_or_create(
                user=user,
                edition=edition,
                platform=random.choice(list(edition.platforms.all())),
                status=random.choice(status_objs),
                defaults={
                    "priority": random.randint(1, 10),
                    "hours_played": random.uniform(0, 200),
                    "notes": "",
                    "start_date": None,
                    "finish_date": None,
                }
            )

            # Add mediums
            lib = Library.objects.get(user=user, edition=edition)
            lib.mediums.set(random.sample(medium_objs, random.randint(1, 2)))

            # Add subscription services (40% chance)
            if random.random() < 0.4:
                lib.subscription_services.set(
                    random.sample(service_objs, random.randint(1, 2))
                )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
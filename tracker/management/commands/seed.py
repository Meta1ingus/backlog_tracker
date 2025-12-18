# tracker/management/commands/seed.py
from django.core.management.base import BaseCommand
from tracker.models import Status, Platform

class Command(BaseCommand):
    def handle(self, *args, **options):
        statuses = [
            ("wishlist", "Wishlist"),
            ("backlog", "Backlog"),
            ("paused", "Paused"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
            ("shelved", "Shelved"),
            ("abandoned", "Abandoned"),
        ]
        for key, label in statuses:
            Status.objects.get_or_create(key=key, label=label)

        platforms = [
            ("PC", "Various", "PC"),
            ("PS5", "Sony", "Console"),
            ("Xbox Series", "Microsoft", "Console"),
            ("Switch", "Nintendo", "Console"),
            ("Steam", "Valve", "Service"),
            ("GOG", "CD Projekt", "Service"),
            ("Epic", "Epic Games", "Service"),
        ]
        for name, manufacturer, type in platforms:
            Platform.objects.get_or_create(name=name, manufacturer=manufacturer, type=type)

        self.stdout.write(self.style.SUCCESS("Seeded statuses and platforms"))
from django.db import models
from django.contrib.auth.models import User

class Platform(models.Model):
    name = models.CharField(max_length=100, unique=True)
    manufacturer = models.CharField(max_length=100, blank=True)
    type = models.CharField(
        max_length=50,
        choices=[("Console", "Console"), ("PC", "PC"), ("Service", "Service")]
    )

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField(null=True, blank=True)
    developer = models.CharField(max_length=200, blank=True)
    publisher = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class Edition(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="editions")
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=50, blank=True)
    release_date = models.DateField(null=True, blank=True)
    platforms = models.ManyToManyField(Platform, related_name="editions")

    def __str__(self):
        return f"{self.game.title} - {self.name}"

class Status(models.Model):
    key = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

    def badge_class(self):
        mapping = {
            "wishlist": "badge-wishlist",
            "backlog": "badge-backlog",
            "paused": "badge-paused",
            "in_progress": "badge-in_progress",
            "completed": "badge-completed",
            "shelved": "badge-shelved",
            "abandoned": "badge-abandoned",
        }
        return mapping.get(self.key, "badge-secondary")

class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="libraries")
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    priority = models.IntegerField(default=5)
    hours_played = models.FloatField(default=0)
    notes = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.edition} ({self.status.label})"
from django.contrib import admin
from .models import Platform, Game, Edition, Status, Library

admin.site.register(Platform)
admin.site.register(Game)
admin.site.register(Edition)
admin.site.register(Status)
admin.site.register(Library)
from django.contrib import admin

from e_shop.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "date"]
    list_filter = ["title", "date"]

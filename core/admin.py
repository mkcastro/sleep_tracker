from django.contrib import admin

from .models import Bed, Coffee, Sleep, Usana


@admin.register(Sleep)
class SleepAdmin(admin.ModelAdmin):
    ordering = ["-woke_at"]


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    pass


@admin.register(Usana)
class UsanaAdmin(admin.ModelAdmin):
    pass

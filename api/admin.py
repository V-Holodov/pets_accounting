from django.contrib import admin

from .models import Pet, PetPhoto


class PetPthotoInline(admin.TabularInline):
    fk_name = "pet"
    model = PetPhoto


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    inlines = [
        PetPthotoInline,
    ]
    search_fields = ("name",)
    list_filter = ("created_at",)

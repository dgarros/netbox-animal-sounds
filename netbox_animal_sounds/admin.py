from django.contrib import admin

from netbox.admin import admin_site
from .models import Animal


@admin.register(Animal, site=admin_site)
class AnimalAdmin(admin.ModelAdmin):
    """
    This class defines a Django administrative view for the Animal model. The register()
    decorator above registers the view with NetBox's admin site object.
    """
    list_display = ('name', 'sound')


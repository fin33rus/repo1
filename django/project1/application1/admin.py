from django.contrib import admin
from application1.models import WahaShop, WahaGame

class Application1Admin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'price')
    list_display_links = ('name', 'short_description')
    search_fields = ('name', 'short_description')

# Register your models here.

admin.site.register(WahaShop)
admin.site.register(WahaGame, Application1Admin)


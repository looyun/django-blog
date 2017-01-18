from django.contrib import admin

# Register your models here.
from .models import ShortURL

class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('url', 'shortcode')

admin.site.register(ShortURL,ShortURLAdmin)
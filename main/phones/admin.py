from django.contrib import admin
from .models import Phone

# Register your models here.

@admin.register(Phone)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'release_date', 'lte_exists']
    list_filter = ['name', 'price', 'lte_exists']
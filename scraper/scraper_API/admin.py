from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    search_fields = ('name', 'address')

admin.site.register(Link, LinkAdmin)

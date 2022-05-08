from django.contrib import admin
from .models import Tag


@admin.register(Tag)
class TaAdmin(admin.ModelAdmin):
    search_fields = ['label']

from django.contrib import admin
from .models import Experience

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'content')

admin.site.register(Experience, ExperienceAdmin)

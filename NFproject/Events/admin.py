from django.contrib import admin

# Register your models here.
from .models import Events


class eventAdmin (admin.ModelAdmin):
    list_display = ('title', 'organizer', 'date')


admin.site.register(Events, eventAdmin)

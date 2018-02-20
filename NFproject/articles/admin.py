from django.contrib import admin

# Register your models here.
from .models import Article

class articleAdmin (admin.ModelAdmin):
  list_display= ('Title','Author','Date_created')


admin.site.register(Article,articleAdmin)

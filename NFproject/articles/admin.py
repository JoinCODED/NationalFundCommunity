from django.contrib import admin

# Register your models here.
from .models import Article

class articleAdmin (admin.ModelAdmin):
  list_display= ('title','author','created_at')


admin.site.register(Article,articleAdmin)

from django.contrib import admin

# Register your models here.
from .models import Article, Category


class articleAdmin (admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(Article, articleAdmin)
admin.site.register(Category)

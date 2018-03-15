from django.contrib import admin

# Register your models here.
from .models import Article, Category, Comments


class articleAdmin (admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(Article, articleAdmin)
admin.site.register(Category)
admin.site.register(Comments)

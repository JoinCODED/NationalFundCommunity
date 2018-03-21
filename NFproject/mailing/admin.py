from django.contrib import admin
from .models import Subscriber



class subscriberAdmin (admin.ModelAdmin):
    list_display = ('email',)


admin.site.register(Subscriber, subscriberAdmin)
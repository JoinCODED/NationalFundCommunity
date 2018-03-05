from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Individual, Organization


admin.site.register(Individual)
admin.site.register(Organization)
admin.site.register(User, UserAdmin)

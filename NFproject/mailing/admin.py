from django.contrib import admin
from django.core.mail import send_mail
from .models import Subscriber

def send_email(modeladmin, request, queryset):
    send_mail(
    'Subscribers',
    'Check our latest articles and events go to our website',
    'copy4ever@yahoo.com',
    ['copy4ever@gmail.com'],
    
    )
    for q in queryset:
        print(q.email)
    send_email.short_description = "Send Email"


class subscriberAdmin (admin.ModelAdmin):
    list_display = ('email',)
    actions = [send_email]


admin.site.register(Subscriber, subscriberAdmin)
from django.contrib import admin
from django.core.mail import send_mail
from .models import Subscriber

def send_email(modeladmin, request, queryset):
    email_list = []
    for q in queryset:
        email_list.append(q.email)
    
    send_mail(
    'Subscribers',
    'Check our latest articles and events on our website',
    'copy4ever@yahoo.com',
     email_list,
    
    )
    
    send_email.short_description = "Send Email"


class subscriberAdmin (admin.ModelAdmin):
    list_display = ('email',)
    actions = [send_email]


admin.site.register(Subscriber, subscriberAdmin)
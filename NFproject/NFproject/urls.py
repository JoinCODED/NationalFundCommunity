"""NFproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import home
from rest_framework import routers

import user_profiles.views as profile_views  # from user_profile import views
import django.contrib.auth.views as auth_views
import api.views as api_views

router = routers.DefaultRouter()
router.register(r'articles', api_views.ArticleViewSet)
router.register(r'events',api_views.EventViewSet)
router.register(r'individuals', api_views.IndividualProfileViewSet)
router.register(r'organizations', api_views.OrganizationProfileViewSet)


urlpatterns = [
    path('', home, name='home'),
    path('articles/', include('articles.urls')),
    path('events/', include('Events.urls')),
    path('profiles/', include('user_profiles.urls')),
    path('signup/', profile_views.signup, name='signup'),  # ,views.signup,

    path('signup/individual',
         profile_views.individual_signup,
         name='individual_signup'),

    path('signup/organization',
         profile_views.organization_signup,
         name='organization_signup'),

    path('login/', auth_views.login, {
        'template_name': 'login.html'
    }, name="login"),

    path('logout/', auth_views.logout, {
        'next_page': '/'
    }, name='logout'),

    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

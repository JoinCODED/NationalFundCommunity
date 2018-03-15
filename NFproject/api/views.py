from django.shortcuts import render
from rest_framework import viewsets
from articles.models import Article
from Events.models import Events
from user_profiles.models import  User, Individual, Organization

from .serializers import ArticleSerializer,ArticleDetailsSerializer,EventSerializer, IndividualProfileListSerializer ,OrganizationProfileListSerializer

# Create your views here.

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        if self.action == 'retrieve':
            return ArticleDetailsSerializer
        return serializers.Default


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer


class IndividualProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Individual.objects.all()
    serializer_class = IndividualProfileListSerializer

class OrganizationProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationProfileListSerializer

from rest_framework import serializers
from articles.models import Article, Category
from Events.models import Events
from user_profiles.models import  User, Individual, Organization



class CategoryListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name
        

class AuthorOfArticle(serializers.RelatedField):
    def to_representation(self, value):
       
        return {
            "Author Name": value.name(),
            "URL": value.get_profile_url()
            
        }
class TypeListField(serializers.RelatedField):
    def to_representation(self, value):
        return  value.name


class EventSerializer(serializers.ModelSerializer):
    event_type = TypeListField(many = False , read_only = True)
    class Meta:
        model = Events
        exclude =('attendees','slug',)

class ArticleSerializer(serializers.ModelSerializer):
    category = CategoryListingField(many=True, read_only=True)
    author = AuthorOfArticle(many = False, read_only = True)
    class Meta:
        model = Article
        fields =['id','title','category','picture','author']

#create the Details Serializer only when you need to customize it,
# if not it will be created by default
class ArticleDetailsSerializer(serializers.ModelSerializer):
    category = CategoryListingField(many=True, read_only=True)
    author = AuthorOfArticle(many = False, read_only = True)
    class Meta:
        model = Article
        fields =['id','title', 'content' , 'created_at','featured','category','picture','author']

class IndividualProfileListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Individual
        fields = ['id','bio','website','interest','first_name','last_name']


class OrganizationProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ['id','bio','website','company_name','location_URL']
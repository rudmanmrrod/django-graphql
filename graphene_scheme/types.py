import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from movies.models import Category, Movie


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = {
            'name': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        filter_fields = {
            'name': ['exact', 'icontains'],
            'year': ['exact'],
            'rating': ['exact'],
            'category__name': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )


class Query(object):
    movie = relay.Node.Field(MovieType)
    all_categories = DjangoFilterConnectionField(CategoryType)
    all_movies = DjangoFilterConnectionField(MovieType)
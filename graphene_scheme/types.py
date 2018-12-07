import graphene

from graphene_django.types import DjangoObjectType

from movies.models import Category, Movie


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie


class Query(object):
    movie = graphene.Field(MovieType,
                              id=graphene.Int(),
                              name=graphene.String())
    all_categories = graphene.List(CategoryType)
    all_movies = graphene.List(MovieType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.select_related('category').all()

    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Movie.objects.select_related('category').get(pk=id)

        if name is not None:
            return Movie.objects.select_related('category').get(name=name)

        return None
from rest_framework import serializers

from . import models


class BookModelSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = models.Book
        fields = ('title', 'price', 'author', 'id', 'slug')
        lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
        # }


class AuthorModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Author
        fields = ('name', 'slug', 'books', 'url')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            'books': {'lookup_field': 'slug'}
        }

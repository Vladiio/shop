from rest_framework import serializers

from . import models


class BookModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Book
        fields = ('title', 'price', 'author')


class AuthorModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 1
        model = models.Author
        fields = ('name', 'books')

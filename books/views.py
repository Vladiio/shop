from rest_framework import generics, mixins, viewsets, pagination
# from rest_framework import mixins
# from rest_framework import viewsets

from . import serializers, models



class BookViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    serializer_class = serializers.BookModelSerializer
    queryset = models.Book.objects.all()
    lookup_field = 'slug'
    pagination_class = pagination.CursorPagination
    page_size = 100


class AuthorViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin
):
    serializer_class = serializers.AuthorModelSerializer
    queryset = models.Author.objects.all()
    lookup_field = 'slug'

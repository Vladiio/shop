from rest_framework import generics, mixins, viewsets, pagination, permissions
# from rest_framework import mixins
# from rest_framework import viewsets

from . import serializers, models


class BookViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.BookModelSerializer
    queryset = models.Book.objects.all()
    lookup_field = 'slug'
    pagination_class = pagination.CursorPagination
    page_size = 100

    def get_queryset(self):
        books_qs = self.queryset
        filterPhrase = self.request.GET.get('filter')
        if filterPhrase:
            books_qs = books_qs.filter(title__icontains=filterPhrase)
        return books_qs


class AuthorViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
):
    serializer_class = serializers.AuthorModelSerializer
    queryset = models.Author.objects.all()
    lookup_field = 'slug'

from django.urls import path, re_path, include

from rest_framework import serializers, routers, viewsets
from books import views as books_views
from api import views as api_views


router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'books', books_views.BookViewSet)
router.register(r'authors', books_views.AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls', namespace='rest_framework'))
]

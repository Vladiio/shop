from django.urls import path, re_path, include

from rest_framework import serializers, routers, viewsets
from rest_framework.authtoken import views as auth_views
from books import views as books_views
from api import views as api_views


router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'books', books_views.BookViewSet)
router.register(r'authors', books_views.AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', auth_views.obtain_auth_token),
    # path('register', api_views.register)
    path('auth', include('rest_framework.urls', namespace='rest_framework'))
]

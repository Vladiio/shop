from django.contrib.auth import get_user_model
from rest_framework import viewsets, decorators, response

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.create()
            return response.Response(status=201, data={'username': serializer.data['username'], 'id': user.id})
        return response.Response(status=400, data=serializer.errors)

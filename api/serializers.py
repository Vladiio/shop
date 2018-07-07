from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
    
    def create(self):
        user = super().create(self.validated_data)
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user

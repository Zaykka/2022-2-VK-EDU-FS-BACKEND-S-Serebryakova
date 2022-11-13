from users.models import User
from users.serializers import UserSerializer
from rest_framework import generics


class UserAPIView(generics.RetrieveAPIView):
    """Получить информацию о пользователях"""

    serializer_class = UserSerializer
    queryset = User.objects.all()

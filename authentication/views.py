from authentication.models import User
from rest_framework import generics
from authentication.serializers import UserCreateUpdateSerializer, UserDetailSerializer


class UserCrateViews(generics.CreateAPIView):
    """UserCreate"""

    serializer_class = UserCreateUpdateSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class UserUpdateViews(generics.RetrieveUpdateAPIView):
    """UserUpdate"""

    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer

    def get_queryset(self):
        """Возвращать объект только для текущего аутентифицированного пользователя"""
        return self.queryset.filter(username=self.request.user)


class UserDetailViews(generics.RetrieveAPIView):
    """ "UserDetail"""

    queryset = User.objects.filter()
    serializer_class = UserDetailSerializer


class UserDeleteViews(generics.RetrieveDestroyAPIView):
    """UserDelete"""

    queryset = User.objects.filter()
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        """Возвращать объект только для текущего аутентифицированного пользователя"""
        return self.queryset.filter(username=self.request.user)

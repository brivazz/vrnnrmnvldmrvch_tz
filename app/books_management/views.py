from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import BookSerializer, UserSerializer
from .models import Book, Author, UserProfile
from .tasks import send_welcome_email


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        author_full_name = data.pop('author_full_name')
        author, _ = Author.objects.get_or_create(full_name=author_full_name)

        book = Book.objects.create(author=author, **data)

        serializer = self.get_serializer(book)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = serializer.instance
        UserProfile.objects.create(user=user)

        send_welcome_email.delay(user.id)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

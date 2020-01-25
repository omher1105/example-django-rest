from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, \
    HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from apps.users.api.serializers import UserSerializers, UserRequestSerializers

APIView


class UserViewSets(APIView):
    serializer_class = UserSerializers
    pagination_class = None

    def get(self, request, pk=None):
        if pk:
            user = User.objects.get(pk=pk)
            serializer = self.serializer_class(user)
        else:
            users = User.objects.all()
            serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, HTTP_200_OK)

    def post(self, request):
        serializer = UserRequestSerializers(data=request.data)
        if serializer.is_valid():
            User.objects.create(**serializer.data)
            return Response(serializer.data, HTTP_201_CREATED)
        else:
            return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        user = User.objects.get(pk=pk)
        user.password = request.data['password']
        user.save()
        serializer = self.serializer_class(user)
        return Response(serializer.data, HTTP_201_CREATED)

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(HTTP_200_OK)

from rest_framework.decorators import api_view
from rest_framework import status, viewsets
from rest_framework.response import Response
from inventory.models import Item
from rest_framework.permissions import IsAuthenticated, AllowAny, SAFE_METHODS
from inventory.serializers import ItemSerializer,  CreateUserSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics

User = get_user_model()


@api_view(['GET'])
def index(request):
    return Response({"msg": "hello, world"}, status=status.HTTP_200_OK)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.filter()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

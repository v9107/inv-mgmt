from rest_framework.decorators import api_view
from rest_framework import status, viewsets
from rest_framework.response import Response
from inventory.models import Item
from rest_framework.permissions import IsAuthenticated
from inventory.serializers import ItemSerializer
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie


@api_view(['GET'])
def index(request):
    return Response({"msg": "hello, world"}, status=status.HTTP_200_OK)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

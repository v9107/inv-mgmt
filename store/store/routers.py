from rest_framework import routers
from inventory import views

router = routers.SimpleRouter()
router.register(r'api/items', views.ItemViewSet, basename="items")

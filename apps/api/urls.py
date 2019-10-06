from rest_framework import routers
from .views import ManualViewSet


router = routers.DefaultRouter()
router.register(r'manual', ManualViewSet)

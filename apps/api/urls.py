from rest_framework import routers
from .views import (UserViewSet, SheetViewSet, PlaceViewSet,
                    TimeViewSet, TaskViewSet, CellViewSet)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sheets', SheetViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'times', TimeViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'cells', CellViewSet)

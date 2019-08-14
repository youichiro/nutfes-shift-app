from rest_framework import routers
from .views import (
    BelongViewSet,
    DepartmentViewSet,
    GradeViewSet,
    MemberViewSet,
    SheetViewSet,
    TimeViewSet,
    TaskViewSet,
    CellViewSet,
    ManualViewSet,
)


router = routers.DefaultRouter()
# router.register(r'belongs', BelongViewSet)
# router.register(r'departments', DepartmentViewSet)
# router.register(r'grades', GradeViewSet)
# router.register(r'members', MemberViewSet)
# router.register(r'sheets', SheetViewSet)
# router.register(r'times', TimeViewSet)
# router.register(r'tasks', TaskViewSet)
# router.register(r'cells', CellViewSet)
# router.register(r'manual', ManualViewSet)

from rest_framework import viewsets
from apps.shift.models import Belong, Department, Grade, Member, Sheet, Time, Task, Cell
from .serializer import (BelongSerializer, DepartmentSerializer, GradeSerializer, MemberSerializer,
                         SheetSerializer, TimeSerializer, TaskSerializer, CellSerializer)


class BelongViewSet(viewsets.ModelViewSet):
    queryset = Belong.objects.all()
    serializer_class = BelongSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class SheetViewSet(viewsets.ModelViewSet):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer


class TimeViewSet(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_fields = ('place', 'color')


class CellViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
    filter_fields = ('sheet', 'member', 'time', 'task')

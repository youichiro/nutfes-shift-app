import  django_filters
from rest_framework import viewsets, filters
from apps.account.models import User, Belong, Department, Grade
from apps.shift.models import Sheet, Place, Time, Task, Cell
from .serializer import (UserSerializer, BelongSerializer, DepartmentSerializer, GradeSerializer, SheetSerializer,
                         PlaceSerializer, TimeSerializer, TaskSerializer, CellSerializer)


class BelongViewSet(viewsets.ModelViewSet):
    queryset = Belong.objects.all()
    serializer_class = BelongSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('name', 'belong', 'department', 'grade')


class SheetViewSet(viewsets.ModelViewSet):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


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
    filter_fields = ('sheet', 'user', 'time', 'task')

from rest_framework import serializers
from apps.account.models import User
from apps.shift.models import Sheet, Place, Time, Task, Cell


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'student_id', 'name', 'belong', 'department', 'grade',
                  'phone_number', 'is_staff', 'is_active', 'is_superuser')


class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheet
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()

    class Meta:
        model = Task
        fields = '__all__'


class CellSerializer(serializers.ModelSerializer):
    sheet = SheetSerializer()
    user = UserSerializer()
    time = TimeSerializer()
    task = TaskSerializer()

    class Meta:
        model = Cell
        fields = '__all__'

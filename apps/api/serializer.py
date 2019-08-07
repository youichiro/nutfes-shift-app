from rest_framework import serializers
from apps.shift.models import Belong, Department, Grade, Member, Sheet, Time, Task, Cell
from apps.manual.models import Manual


class BelongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Belong
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheet
        fields = '__all__'


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CellSerializer(serializers.ModelSerializer):
    sheet = SheetSerializer()
    member = MemberSerializer()
    time = TimeSerializer()
    task = TaskSerializer()

    class Meta:
        model = Cell
        fields = '__all__'


class ManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual
        fields = '__all__'

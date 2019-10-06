from rest_framework import serializers
from apps.manual.models import Manual


class ManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual
        fields = '__all__'

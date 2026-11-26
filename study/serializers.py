from rest_framework import serializers
from .models import Faculty, Direction, Manager

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'name', 'description')

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class DirectionManagerSerializer(serializers.ModelSerializer):
    class Meta:
         model = Manager  # укажите нужную модель
         fields = '__all__'
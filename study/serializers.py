from rest_framework import serializers
from study.models import Faculty, Student, Direction, DirectionManager

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '_all_'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '_all_'

class DirectionSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(read_only=True)

    class Meta:
        model = Direction
        fields = '_all_'

class DirectionManagerSerializer(serializers.ModelSerializer):
    direction = DirectionSerializer(read_only=True)

    class Meta:
        model = DirectionManager
        fields = '_all_'
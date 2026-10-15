from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Faculty, Student, Direction, DirectionManager
from .serializers import (
    FacultySerializer,
    StudentSerializer,
    DirectionSerializer,
    DirectionManagerSerializer,
)

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

class DirectionManagerViewSet(viewsets.ModelViewSet):
    queryset = DirectionManager.objects.all()
    serializer_class = DirectionManagerSerializer
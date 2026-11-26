
from rest_framework import viewsets, mixins
from .models import Student, DirectionManager
from .serializers import *

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DirectionViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

class DirectionManagerViewSet(viewsets.ModelViewSet):
    queryset = DirectionManager.objects.all()
    serializer_class = DirectionManagerSerializer
from django.shortcuts import render

# Create your views here.

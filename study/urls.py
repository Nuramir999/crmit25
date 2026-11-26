from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'directions', DirectionViewSet)
router.register(r'faculty', FacultyViewSet)
router.register(r'students', StudentViewSet)
router.register(r'direction-manager', DirectionManagerViewSet)
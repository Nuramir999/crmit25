from django.contrib import admin
from study.models import Faculty, Speciality,Manager





@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    pass


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    pass

@admin.register(Manager)
class DirectionManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'direction')
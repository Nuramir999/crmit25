from django.contrib import admin
from django.db.migrations.operations import special

from study.models import Faculty, Speciality, SpecialityManager


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    pass

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    pass


@admin.register(SpecialityManager)
class ManagerAdmin(admin.ModelAdmin):
    pass

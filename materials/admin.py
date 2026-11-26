# Register your models here.
from django.contrib import admin

from materials.models import StudyTest, Material, Task, TestQuestion


# Register your models here.

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(StudyTest)
class StudyTestAdmin(admin.ModelAdmin):
    pass

@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    pass
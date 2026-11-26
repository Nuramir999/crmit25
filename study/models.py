from django.db import models


class Faculty(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.name

class Direction(models.Model):
    objects = None
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.name

class DirectionManager(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    direction = models.OneToOneField(Direction, on_delete=models.CASCADE, default=1)

    def _str_(self):
        return self.name



GENDER_CHOICES ={
    ('M', 'Male'),
    ('F', 'Female'),
}
class Student(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    direction = models.ManyToManyField(Direction, related_name="students_direction")
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=True)
    def __str__(self):
        return self.name



class Speciality(models.Model):
    name = models.CharField(max_length=100, verbose_name="название специальности")
    direction = models.TextField(blank=True, null=True, verbose_name="описание")


    def _str_(self):
        return self.name

class Manager(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя менеджера")
    age = models.IntegerField(verbose_name="Возраст", null=True, blank=True)
    direction = models.TextField(verbose_name="Направление", blank=True, null=True)

    def _str_(self):
        return self.name
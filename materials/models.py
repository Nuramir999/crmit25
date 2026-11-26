# Create your models here.
from django.db import models

# Create your models here.

class Material(models.Model):
    text = models.TextField()
    file = models.TextField()

class Task(models.Model):
    description = models.TextField()
    deadline = models.DateTimeField()

class StudyTest(models.Model):
    name = models.CharField(max_length=255)

class TestQuestion(models.Model):
    text  = models.TextField()
    study = models.ForeignKey(StudyTest, on_delete=models.CASCADE)

class TestQuestionAnswer(models.Model):
    answer = models.CharField(max_length=50)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, null=True, blank=True)
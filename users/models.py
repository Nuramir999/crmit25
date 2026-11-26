

from django.contrib.auth import models
from django.contrib.auth.models import AbstractUser
from study.models import GENDER_CHOICES


class User(AbstractUser):
    age =  models.IntegerField()
    gender = models.Charfield(max_length=50, choices=GENDER_CHOICES)



# Create your models here.

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Disciplines(models.Model):
    name = models.CharField(max_length=200)


class Books(models.Model):
    name = models.CharField(max_length=200)
    discipline = models.ForeignKey(Disciplines, on_delete=models.CASCADE)


class UserDiscipline(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discip = models.ForeignKey(Disciplines, on_delete=models.CASCADE)


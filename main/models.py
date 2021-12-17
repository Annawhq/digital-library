from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Disciplines(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='')
    nomer = models.CharField(max_length=17, default='')
    link = models.URLField(default='')
    discipline = models.ForeignKey(Disciplines, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserDiscipline(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discip = models.ForeignKey(Disciplines, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


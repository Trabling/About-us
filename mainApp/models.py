from django.db import models

class Teammate(models.Model):
  Name = models.CharField(max_length=50)
  Birth = models.DateField()
  Nickname = models.CharField(max_length=50)
  Major = models.CharField(max_length=50)
  MBTI = models.CharField(max_length=50)
  Hobby = models.TextField()
  Food = models.TextField()
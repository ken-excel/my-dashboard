from django.db import models

class Computer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Temperature(models.Model):
    name = models.CharField(max_length=50, unique=True)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    temperature = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Fan(models.Model):
    name = models.CharField(max_length=50, unique=True)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    speed = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Crypto(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
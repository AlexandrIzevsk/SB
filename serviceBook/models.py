from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=20, unique=True)
    descriptions = models.TextField()

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')


class Manual(models.Model):
    nameClass = models.CharField(max_length=20)
    name = models.CharField(max_length=20, unique=True)
    descriptions = models.TextField()

    def __str__(self):
        return f'{self.name}: {self.descriptions}'


class Machine(models.Model):
    zavNumberMachine = models.CharField(max_length=20, unique=True)
    modelMachine = models.ForeignKey(Manual, on_delete=models.CASCADE, related_name='modelMachine')
    modelMotor = models.ForeignKey(Manual, on_delete=models.CASCADE, related_name='modelMotor')
    zavNumberMotor = models.CharField(max_length=20)
    modelTransmission = models.ForeignKey(Manual, on_delete=models.CASCADE, related_name='modelTransmission')
    zavNumberTransmission = models.CharField(max_length=20)
    modelDriveAxile = models.ForeignKey(Manual, on_delete=models.CASCADE, related_name='modelDriveAxile')
    zavNumberDA = models.CharField(max_length=20)
    modelControllAxile = models.ForeignKey(Manual, on_delete=models.CASCADE, related_name='modelControllAxile')
    zavNumberCA = models.CharField(max_length=20)
    deliveryContract = models.CharField(max_length=50)
    shipDate = models.DateTimeField(auto_now_add=True)
    recipient = models.CharField(max_length=100)
    deliveryAddress = models.CharField(max_length=150)
    package = models.TextField(blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


# Create your models here.

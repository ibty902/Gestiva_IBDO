from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    ville = models.CharField(max_length=100)
from django.db import models
from django.urls import path

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

# Create your models here.

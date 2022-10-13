from enum import unique
from django.db import models

# Create your models here.

class Work_Area(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
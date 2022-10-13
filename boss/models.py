from django.db import models

from workArea.models import Work_Area

# Create your models here.

class Boss(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    salary = models.IntegerField()
    phone = models.CharField(max_length=13)
    dni = models.CharField(max_length=10)
    image = models.ImageField(upload_to="boss", default='images.jpeg')
    boss_area = models.ForeignKey(Work_Area, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
from django.db import models

# Create your models here.

class Shelters(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    link=models.CharField(max_length=100)
    max_size=models.IntegerField(default=100)
    current_size=models.IntegerField(default=100)
    image=models.ImageField(upload_to="shimages",null=True,blank=True)
def __str__(self):
    return self.name

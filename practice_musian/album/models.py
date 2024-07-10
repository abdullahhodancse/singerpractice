
from django.db import models
from singer.models import Singer 
 

# Create your models here.
class Album(models.Model):
   Album_Name = models.CharField(max_length=100)
   Album_release_date = models.DateTimeField()
   Rating = models.DecimalField(max_digits=5, decimal_places=2)
   singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
  


   def __str__(self):
    return  self.Album_Name


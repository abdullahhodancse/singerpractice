from django.db import models
 

# Create your models here.
class Singer(models.Model):
   First_Name = models.CharField(max_length=100)
   Last_Name = models.CharField(max_length=100)
   Email=models.EmailField()
   Phone=models.CharField(max_length=11)
   instrument=models.CharField(max_length=110)
  
   
  


   def __str__(self):
    return  self.First_Name


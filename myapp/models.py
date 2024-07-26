from django.db import models

# Create your models here.

class Info(models.Model):
    firstname=models.CharField(max_length=20)
    startdate=models.DateField()
    enddate=models.DateField()
    status=models.CharField(max_length=20)
    
    def __str__(self):
        return self.firstname
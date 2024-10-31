from django.db import models

class people_details(models.Model):
    name=models.CharField(max_length=20,blank=False)
    gender=models.CharField(max_length=10,blank=False)
    place=models.CharField(max_length=50,blank=False)
    age=models.PositiveIntegerField(default=25)

    class Meta:
        db_table="people_details"

    

    

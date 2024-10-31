from django.db import models
class team(models.Model):
    team_name=models.CharField(max_length=30)
    team_color=models.CharField(max_length=20)

    class Meta:
        db_table="team"

class people_details(models.Model):
    name=models.CharField(max_length=20,blank=False)
    gender=models.CharField(max_length=10,blank=False)
    place=models.CharField(max_length=50,blank=False)
    age=models.PositiveIntegerField(default=25)
    team=models.ForeignKey(team,on_delete=models.CASCADE,null=True,blank=True,default=None)

    class Meta:
        db_table="people_details"

    

    

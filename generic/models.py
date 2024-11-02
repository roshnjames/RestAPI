from django.db import models

class blogmodel(models.Model):
    name=models.CharField(max_length=30)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=20)
    timestamp=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="blogmodel"
        
    def __str__(self):
        return self.title

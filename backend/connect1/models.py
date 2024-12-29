from django.db import models

class UserDetails(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    profile=models.ImageField(upload_to='profiles/',default='xxx')
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=60)
    timestamp=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='UserDetails'

    def __str__(self):
        return self.username
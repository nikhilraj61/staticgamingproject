from django.db import models
import datetime

# Create your models here.
class shop(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    desc=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='picture')
   


    def __str__(self):
        return self.name

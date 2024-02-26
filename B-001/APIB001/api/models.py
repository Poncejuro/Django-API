from django.db import models

# Create your models here.

class BlogPost(models.Model):
    ID = models.AutoField(primary_key=True)
    title=models.CharField(max_length=500)
    link=models.CharField(max_length=500)
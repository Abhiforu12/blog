from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=1000)


    def __str__(self):
        return self.title
    

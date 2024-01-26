from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=10000)
    img = models.ImageField( upload_to='article_images/',default= "dfault_imag.jpg")

    pub_date = models.DateField( auto_now=True)




    def __str__(self):
        return self.title
    

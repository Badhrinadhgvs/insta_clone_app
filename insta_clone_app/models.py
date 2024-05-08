from django.db import models

# Create your models here.


class model1(models.Model):
    name=models.CharField(max_length=2000)
    description=models.CharField(max_length=200000)
    image=models.ImageField(null=True,blank=True)
    
    
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url  
    
    

class Photo(models.Model):
    image = models.ImageField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    Title=models.CharField(null=True,max_length=50)

    def __str__(self):
        return f"Photo {self.id}"    
from django.db import models
from django.urls import reverse
from PIL import Image

class Mobile(models.Model):
    name = models.CharField(max_length=50)
    price =models.CharField(max_length=10)
    cam_des = models.TextField(default = 'NA')
    RAM_des = models.TextField(default = 'NA')
    image = models.ImageField(default = 'cart.jpg', upload_to = 'mobile_pics')
    
    def save(self, *args, **kwargs):
        super().save()
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
       
    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})
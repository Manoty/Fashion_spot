from django.db import models
from PIL import Image

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    qtty = models.CharField(max_length=100, blank=False, null=False)
    price = models.CharField(max_length=100, blank=False, null=False)
    desc = models.CharField(max_length=300, blank=False, null=False)
    image= models.ImageField(upload_to='static/images/products/')


    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height < 500 or img.width <350:
            output_size = (500, 350)
            img.thumbnail(output_size)
            img.save(self.image.path)

def __str__(self):
    return self.name
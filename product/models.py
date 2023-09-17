from django.db import models
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', default='')
    

    def __str__(self):
        return self.name
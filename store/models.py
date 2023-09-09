from django.db import models

class CustomerTestimonial(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.name

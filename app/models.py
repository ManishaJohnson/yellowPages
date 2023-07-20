from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name= models.CharField(max_length=100)
    ph1=models.TextField()
    ph2=models.TextField()
    def __str__(self):
        return self.name
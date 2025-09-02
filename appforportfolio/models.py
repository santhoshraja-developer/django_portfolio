from django.db import models

# Create your models here.

class Contactmessage (models.Model):
    name =models.CharField(max_length=100)
    email=models.EmailField()
    subject = models.CharField(max_length=200)
    message = models. TextField(max_length=3000)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fullname

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
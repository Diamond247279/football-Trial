from enum import unique
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-id']
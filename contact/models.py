from django.db import models
import datetime

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_contacted = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
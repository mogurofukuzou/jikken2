from django.db import models

# Create your models here.


class Manager(models.Model):
    name = models.CharField(max_length=50)
    username = models.TextField()
    email = models.TextField(default="")

    def __str__(self):
        return self.name

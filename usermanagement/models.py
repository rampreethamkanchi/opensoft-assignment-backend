from django.db import models
class user(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,unique=True)
    def __str__(self):
        return self.username
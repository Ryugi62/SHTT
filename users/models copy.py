from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)

    username = models.CharField(max_length=50, unique=True)
    nickname = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
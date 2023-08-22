from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique = True)
    avatar = models.ImageField(null = True , default = 'avatar.svg')
    
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    


class Test(models.Model):
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    


    

    

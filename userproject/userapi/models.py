from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=70, blank=False, default='')
    senha = models.CharField(max_length=12, blank=False, default='')
    data_nascimento = models.DateField(blank=False)
    

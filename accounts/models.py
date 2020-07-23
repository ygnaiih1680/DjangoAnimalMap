from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
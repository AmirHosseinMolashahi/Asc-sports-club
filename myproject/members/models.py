from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Coaches(models.Model):
    COACHES_GENDER = (
        ('male', 'male'),
        ('female', 'female'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birthday = models.DateField()
    image = models.ImageField(upload_to="members/coaches")
    description = models.TextField()
    coaching_time = models.DateField()
    sports_that_teach = models.CharField(max_length=1000)
    gender = models.CharField(max_length=10, choices=COACHES_GENDER)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class transportmodel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Rideshare = "Rideshare"
    Public = "Public"
    role_CHOICES = [
        (Rideshare, 'Rideshare'),
        (Public, 'Public'),
        ]
    role = models.CharField(
        max_length=10,
        choices=role_CHOICES,
        default= Public
    )
    def __str__(self):
        return f"{self.user} is taking {self.role}"
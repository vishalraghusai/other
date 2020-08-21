from django.db import models

# Create your models here.

class user(models.Model):
    F_name = models.CharField(max_length=20)
    L_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email or self.F_name or self.L_name

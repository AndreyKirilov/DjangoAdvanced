from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(validators=[MinLengthValidator(5), ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=3, decimal_places=2, null=True)

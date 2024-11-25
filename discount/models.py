from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Discount(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)])
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.code)

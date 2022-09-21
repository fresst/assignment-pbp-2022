from decimal import Decimal
from platform import release
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.DecimalField( 
                default=1,
                max_digits=3,
                decimal_places=2,
                validators=[
                    MinValueValidator(Decimal('1.00')),
                    MaxValueValidator(Decimal('5.00'))
                ]              
            )
    release_date = models.DateField()
    review = models.TextField()
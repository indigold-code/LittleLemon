from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Booking(models.Model):
    ID = models.IntegerField(primary_key=True, unique=True, validators=[MaxValueValidator(99999999999)],default=0)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(validators=[MaxValueValidator(6)])
    BookingDate = models.DateTimeField() 



class Menu(models.Model):
    MenuID = models.IntegerField(primary_key=True, unique=True, validators=[MaxValueValidator(99999)], default=0)
    Title = models.CharField(max_length=255, unique=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(validators=[MaxValueValidator(99999)])

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)

class FuelType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)

class ClothingType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)

class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    minimum_offer = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    photo = models.ImageField()
    description = models.CharField(max_length=2000, blank=True)
    cell = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    messages_allowed = models.BooleanField(default=False)
    liked = models.BooleanField(default=False)
    only_available_on_call = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

class Residence(Item):
    num_bedrooms = models.IntegerField(validators=[MaxValueValidator(9), MinValueValidator(1)])
    num_bathrooms = models.IntegerField(validators=[MaxValueValidator(9), MinValueValidator(1)])
    square_footage = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)])
    lease_duration = models.IntegerField(default=12, validators=[MinValueValidator(1)])

    def __str__(self):
        return super().__str__()

class Vehicle(Item):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField(validators=[MaxValueValidator(2999), MinValueValidator(1900)])
    mileage = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(0)])
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()

class Toy(Item):
    def __str__(self):
        return super().__str__()

class Clothing(Item):
    type = models.ForeignKey(ClothingType, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()

class Electronic(Item):
    def __str__(self):
        return super().__str__()

class Pet(Item):
    def __str__(self):
        return super().__str__()

class Furniture(Item):
    def __str__(self):
        return super().__str__()

class Misc(Item):
    def __str__(self):
        return super().__str__()

class Service(Item):
    def __str__(self):
        return super().__str__()

class Job(Item):
    def __str__(self):
        return super().__str__()

class Book(Item):
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()

class SportingGood(Item):
    def __str__(self):
        return super().__str__()


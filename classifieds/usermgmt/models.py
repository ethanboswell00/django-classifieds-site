from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    header = models.CharField(max_length=200)
    content = models.CharField(max_length=5000, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    listing = models.ForeignKey('listings.Item', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    sent_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.header)

class Offer(models.Model):
    offer_amount = models.DecimalField(max_digits=5, decimal_places=2)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    sent_time = models.DateTimeField(auto_now=True)
    listing = models.ForeignKey('listings.Item', on_delete=models.CASCADE)

class Gender(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    num_listings = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=30)
    profile_photo = models.ImageField()
    num_notifications = models.IntegerField(default=0)
    photo_public = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user.username)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_urgent = models.BooleanField(default=False)
    header = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.header)

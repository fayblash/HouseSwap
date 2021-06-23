from django.db import models
from listings.models import Listing
from accounts.models import Profile

# Create your models here.
class Review(models.Model):
    listing=models.ForeignKey(Listing, on_delete=models.CASCADE)
    author=models.ForeignKey(Profile, on_delete=models.CASCADE)
    text=models.TextField()
    date=models.DateField(auto_now_add=True)
    
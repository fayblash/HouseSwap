from django.db import models
from accounts.models import Profile

# Create your models here.
class Testimonial(models.Model):
    author=models.ForeignKey(Profile, on_delete=models.CASCADE)
    text=models.TextField()
    date=models.DateField(auto_now_add=True)
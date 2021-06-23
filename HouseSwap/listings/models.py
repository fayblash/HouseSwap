from django.db import models
from accounts.models import Profile
from model_utils import Choices
from django.utils.translation import ugettext_lazy  as _

# Create your models here.
class Listing(models.Model):
    host=models.ForeignKey(Profile, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    img_main=models.ImageField(upload_to='photos/%Y/%m/%d/',default='photos/default.png')
    img_2=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    img_3=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    img_4=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description=models.TextField()
    city=models.CharField(max_length=100)
    REGION=Choices(('Jerusalem', _('Jerusalem')), ('Center', _('Center')), ('Eilat', _('Eilat')), ('South', _('South')), ('North', _('North')),)
    region = models.CharField(choices=REGION, default=REGION.North, max_length=20)
    sleeps=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.IntegerField()
    pets=models.BooleanField(default=False)
    kosher=models.BooleanField(default=False)
    pool=models.BooleanField(default=False)
    accessible=models.BooleanField(default=False)
        
    def __str__(self):
        return self.title    
    

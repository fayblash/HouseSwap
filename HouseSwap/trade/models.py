from django.db import models
from accounts.models import *
from listings.models import *
from django.utils.translation import ugettext_lazy  as _
# Create your models here.

class Offer(models.Model):
    host1=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='host1')
    listing1=models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing1')
    host2=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='host2') 
    listing2=models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing2')
    text=models.TextField(blank=True)
    STATUS=Choices(('Pending', _('Pending')), ('Accepted', _('Accepted')), ('Rejected', _('Rejected')))
    status = models.CharField(choices=STATUS, default=STATUS.Pending, max_length=20)
    date_created=models.DateField(auto_now_add=True)

from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from listings.models import Listing
from trade.models import Offer
from testimonials.models import Testimonial
from django.contrib.auth.decorators import login_required
from listings.forms import ListingForm
from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def index(request):
    listings=Listing.objects.order_by('-title')[:6]
    testimonials = Testimonial.objects.all
    context={'listings':listings,  'testimonials':testimonials}
    return render(request,'pages\index.html',context)
 
@login_required
def dashboard(request):
    user=request.user.profile 
    listings = Listing.objects.filter(host=user)
    testimonials = Testimonial.objects.filter(author=user)
    offers=Offer.objects.filter(status="Pending").filter(host1=user)
    requests=Offer.objects.filter(status="Pending").filter(host2=user)
    history=Offer.objects.filter(Q(status__in=('Accepted','Rejected')))
    
    context={'listings':listings,'offers':offers,'requests':requests, 'testimonials':testimonials}
    return render(request, "pages\dashboard.html", context)
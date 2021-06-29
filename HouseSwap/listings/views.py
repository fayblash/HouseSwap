from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,ListView,DetailView,FormView,View,UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Listing
from review.models import Review
from .forms import * 
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory, modelformset_factory
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def add_listing(request):  
    user = request.user.profile 
    form=ListingForm
    if request.method == "POST":
        form = ListingForm(request.POST,request.FILES)
        data=request.POST
        if form.is_valid():
            listing = form.save(commit=False)
            listing.host = user
            listing.save()
            messages.success(request,'Listing Added')
            return redirect('dashboard')
        else:
            messages.error(request, 'Bad form input')
    return render(request, 'listings/add_listing.html', {'form':form})
      
def update_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request,'Listing Updated')
            return redirect("dashboard")
    return render(request, 'listings/update_listing.html', {"form": form})

def delete_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    messages.success(request,'Listing Deleted')
    return redirect("dashboard")

def listing(request, pk):
    listing=get_object_or_404(Listing,id=pk) 
    reviews=Review.objects.filter(listing=pk)
    context={'listing':listing, 'reviews':reviews,}
    return render(request,'listings/listing.html',context) 
    

def listings(request):
    listings=Listing.objects.order_by('-title')
    paginator=Paginator(listings,3)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    
    region_choices={
        'Jerusalem':'Jerusalem',
        'Center':'Center',
        'Eilat':'Eilat',
        'South':'South',
        'North':'North',
    }
    context={
        'listings':paged_listings,
        'region_choices':region_choices,
    }
 
    return render(request,'listings/listings.html',context) 

def search(request):
    queryset_list=Listing.objects.order_by('-title')
    
    #keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)
    
    #city
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact=city)
    
    #region
    if 'region' in request.GET:
        region=request.GET['region']
        if region:
            queryset_list=queryset_list.filter(region__iexact=region)
    
    #number of ppl
    if 'sleeps' in request.GET:
        sleeps=request.GET['sleeps']
        if sleeps:
            queryset_list=queryset_list.filter(sleeps__gte=sleeps)
    
    context={'listings':queryset_list,
             'values':request.GET,
    }
    return render(request,'listings/search.html', context)

def message(request, pk):
    
    
    return render(request,'listings/listing.html',context)
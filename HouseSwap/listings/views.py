from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,ListView,DetailView,FormView,View,UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Listing
from review.models import Review
from .forms import * 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory, modelformset_factory
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
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
    # reviews=Review.objects.get(listing=listing)
    context={'listing':listing}
    return render(request,'listings/listing.html',context) 
    

def listings(request):
    listings=Listing.objects.all
    context={'listings':listings}
    return render(request,'listings/listings.html',context) 
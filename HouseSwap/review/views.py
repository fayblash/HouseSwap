from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *
from listings.models import *
from datetime import date

# Create your views here.
def add_review(request,pk): 
    user = request.user.profile 
    listing=Listing.objects.get(id=pk)
    form=ReviewForm
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = user
            review.listing=listing
            review.save()
            messages.success(request,'Review Added')
            return redirect('dashboard')
        else:
            messages.error(request, 'Bad form input')
    return render(request, 'reviews/add_review.html', {'form':form, 'listing':listing})

def update_review(request,pk):
    review = Review.objects.get(id=pk)
    form = ReviewForm(instance=review)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review=form.save(commit=False)
            review.date=date.today()
            review.save()
            messages.success(request,'Review Updated')
            return redirect("dashboard")
    return render(request, 'reviews/update_review.html', {"form": form, "review":review})

def delete_review(request,pk):
    review=Review.objects.get(id=pk)
    review.delete()
    messages.success(request,'Review Deleted')
    return redirect("dashboard")

    

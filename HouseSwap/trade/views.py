from django.shortcuts import render,redirect
from .models import *
from listings.models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def offer_trade(request,pk): 
    listing2=Listing.objects.get(id=pk)
    host1 = request.user.profile 
    form=OfferForm(request.user)
    if request.method == "POST":
        form = OfferForm(request.user,request.POST)
        data=request.POST
        print(data)
        if form.is_valid():
            offer = form.save(commit=False)
            print(offer)
            offer.host1 = host1
            offer.listing2=listing2
            offer.host2=listing2.host
            offer.save()
            messages.success(request,'Offer Created')
            return redirect('dashboard')
        else:
            messages.error(request, 'Bad form input')
    return render(request, 'trade/offer_trade.html', {'form':form, 'listing':listing2}) 
 

def update_offer(request,pk):
    offer = Offer.objects.get(id=pk)
    form = UpdateOfferForm(instance=offer)
    if request.method == "POST":
        form = UpdateOfferForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    return render(request, 'trade/update_offer.html', {"form": form}) 

def accept_offer(request,pk):
    offer=Offer.objects.get(id=pk)
    offer.status = 'Approved'
    offer.save()
    messages.success(request,'Offer Accepted! Added to your Swaps')
    return redirect ('dashboard')
    
def reject_offer(request,pk):
    offer=Offer.objects.get(id=pk)
    offer.status = 'Rejected'
    offer.save()
    return redirect ('dashboard')

def delete_offer(request,pk):
    offer=Offer.objects.get(id=pk)
    offer.delete()
    return redirect ('dashboard')
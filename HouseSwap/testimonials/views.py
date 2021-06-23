from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def add_testimonial(request):
    testimonial = Testimonial(author=request.user.profile)  
    form = TestimonialForm(instance=testimonial)
    if request.method == "POST":
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            testimonial.save()
            return redirect("dashboard")
    return render(request, 'testimonials/add_testimonial.html', {"form": form})

def update_testimonial(request, pk):
    testimonial = Testimonial.objects.get(id=pk)
    form = TestimonialForm(instance=testimonial)
    if request.method == "POST":
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    return render(request, 'testimonials/update_testimonial.html', {"form": form})

def delete_testimonial(request, pk):
    testimonial = Testimonial.objects.get(id=pk)
    testimonial.delete()
    return redirect("dashboard")  
 
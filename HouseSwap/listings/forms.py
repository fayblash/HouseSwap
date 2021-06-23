from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model=Listing
        fields=['title','img_main','img_2','img_3','img_4','description', 'city','region','sleeps','bathrooms','bedrooms','kosher','pool','accessible','pets',
        ]
         
       
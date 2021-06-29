from django import forms
from .models import Offer
from listings.models import Listing

class OfferForm(forms.ModelForm):
        
    def __init__(self, user, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        self.fields['listing1'].queryset = Listing.objects.filter(host=user.profile)
        
    class Meta:
        model = Offer
        fields = ['listing1','listing2','text','status']
         
class UpdateOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['text']
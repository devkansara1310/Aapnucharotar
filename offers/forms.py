from django import forms
from .models import offers
from django.forms.widgets import NumberInput

class OfferForm(forms.ModelForm):
    class Meta:
        model = offers
        fields = '__all__'
        labels = {
            'name': 'Offer Name',
            'code': 'Offer Code',
            'end': 'End Date',
            'Contact': 'Contanct No.',
            'image': 'Image  ',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Offer Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'xyz@gmail.com'}),
            'end': forms.DateInput(format='%Y/%m/%d', attrs={'title': 'Search'}),
            'status': forms.TextInput(attrs={'id': 'status', 'type': 'hidden'}),
            'vendor1': forms.TextInput(attrs={'id': 'user', 'type': 'hidden'}),
        }

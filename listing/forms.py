from django import forms
from .models import listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = listing
        fields = '__all__'
        labels = {
            'cno': 'Contact No.',
            'Pin': 'Pin Code',
            'image': 'Image  ',
        }
        widgets = {
            'cno': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'id': 'status', 'type': 'hidden'}),
            'lister': forms.TextInput(attrs={'id': 'user', 'type': 'hidden'}),
        }

from django import forms
from .models import doner
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DonationForm(forms.ModelForm):
    class Meta:
        model = doner
        fields = ('name', 'email', 'cno', 'address', 'city', 'pin', 'State', 'Amount')

        def save(self):
            name = self.cleaned_data.get('name')
            Amount = self.cleaned_data.get('Amount')

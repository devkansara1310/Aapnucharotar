from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Blogger, customer, lister, vendor


class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    # transactions is done than it will store in data base
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        Customer = customer.objects.create(user=user)
        Customer.phone_number = self.cleaned_data.get('phone_number')
        Customer.address = self.cleaned_data.get('address')
        Customer.email = self.cleaned_data.get('email')
        Customer.save()
        return user


class BloggerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_blogger = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        blogger = Blogger.objects.create(user=user)
        blogger.phone_number = self.cleaned_data.get('phone_number')
        blogger.designation = self.cleaned_data.get('designation')
        blogger.email = self.cleaned_data.get('email')
        blogger.save()
        return user


class listerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_lister = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        Lister = lister.objects.create(user=user)
        Lister.phone_number = self.cleaned_data.get('phone_number')
        Lister.designation = self.cleaned_data.get('designation')
        Lister.email = self.cleaned_data.get('email')
        Lister.save()
        return user


class vendorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vendor = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        Vendor = vendor.objects.create(user=user)
        Vendor.phone_number = self.cleaned_data.get('phone_number')
        Vendor.designation = self.cleaned_data.get('designation')
        Vendor.email = self.cleaned_data.get('email')
        Vendor.save()
        return user

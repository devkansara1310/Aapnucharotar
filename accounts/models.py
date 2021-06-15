from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

cno = RegexValidator(r'^\+?1?\d{10}$', "Phone number must be entered in the format: '+9999999999'")

class User(AbstractUser):
    is_blogger = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_lister = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(validators=[cno], max_length=10)
    location = models.CharField(max_length=20)


class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(validators=[cno], max_length=10)
    designation = models.CharField(max_length=20)

    # @staticmethod
    # def get_customer(email):
    #     return customer.objects.get(email = email)

class lister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(validators=[cno], max_length=10)
    designation = models.CharField(validators=[cno], max_length=10)


class vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(validators=[cno], max_length=10)
    designation = models.CharField(max_length=20)

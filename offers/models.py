from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from accounts.models import User
from django.core.validators import RegexValidator

cno = RegexValidator(r'^[0-9]', "Phone number must be entered in the format: '9999999999'")

# Create your models here.

class Categoryoffers(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_offers():
        return Categoryoffers.objects.all()


city = [('Nadiad', 'Nadiad'), ('Anand', 'Anand'), ('Borsad', 'Borsad')]

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]

class offers(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=20, unique=True)
    image = models.FileField(upload_to='images/', null=True, verbose_name="")
    Description = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    end = models.DateField(auto_now_add=False)
    Category = models.ForeignKey('Categoryoffers', on_delete=models.CASCADE)
    Contact = models.CharField(validators=[cno], max_length=10)
    email = models.EmailField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True, choices=city, default="Anand")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='d')
    vendor1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendor1')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile')

    @staticmethod
    def get_offer():
        return offers.objects.all()

    @staticmethod
    def get_all_offers():
        return offers.objects.all().order_by('id')[:8]

    @staticmethod
    def get_all_offers_by_id(category_id):
        if category_id:
            return offers.objects.filter(category=category_id)
        else:
            return offers.get_all_offers()


from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator

cno = RegexValidator(r'^[0-9]', "Phone number must be entered in the format: '9999999999'")

class donation_category(models.Model):
    category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category

class donations(models.Model):
    category = models.ForeignKey(donation_category, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/donation', height_field=None, width_field=None, max_length=100,)

    def __str__(self):
        return self.description


city = [('Anand', 'Anand'), ('Nadiad', 'Nadiad')]


class doner(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    cno = models.CharField(validators=[cno], max_length=10)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, choices=city, default='Anand')
    pin = models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    Amount = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

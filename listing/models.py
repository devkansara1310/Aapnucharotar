from django.db import models
from django.urls import reverse
from accounts.models import User
from django.core.validators import RegexValidator

cno = RegexValidator(r'^[0-9]', "Phone number must be entered in the format: '9999999999'")

city = [('Anand', 'Anand'), ('Nadiad', 'Nadiad')]


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    # @staticmethod
    # def get_all_listing():
    #     return Category.objects.all()

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)

    @staticmethod
    def get_all_cat():
        return Sub_Category.objects.all()

    def __str__(self):
        return self.name

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]

class listing(models.Model):
    title = models.CharField(max_length=255,unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    lister_name = models.CharField(max_length=255)
    cno = models.CharField(validators=[cno], max_length=10)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=255, choices=city, default='Anand')
    Pin = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.FileField(upload_to='images/', null=True, verbose_name="")
    open_time = models.TimeField()
    close_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='d')
    lister = models.ForeignKey(User, on_delete=models.CASCADE, related_name='list')

    def get_absolute_url(self):
        return reverse('listing')

    @staticmethod
    def get_listing():
        return listing.objects.all()

    @staticmethod
    def get_all_listing_cat():
        return listing.objects.filter(status='p')

    @staticmethod
    def get_all_listing():
        return listing.objects.filter(status='p').order_by('id')[:8]

    @staticmethod
    def get_all_listing_by_id(categoryName):
        if categoryName:
            return listing.objects.filter(Category=categoryName)
        else:
            return listing.get_all_blog()

    def __str__(self):
        return self.title


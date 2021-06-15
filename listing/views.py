from django.shortcuts import render
from .models import listing, Category, Sub_Category
from django.views.generic import UpdateView, CreateView, DetailView, DeleteView, ListView
from .forms import ListingForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.



def listing01(request):
    list_categories = Category.objects.all()
    categoryName = request.GET.get('category')
    if categoryName:
        listing1 = listing.get_all_listing_by_id(categoryName)
        data1 = {'listing1': listing1, 'lcategories': list_categories}
        return render(request, 'listing_cat.html', data1)
    else:
        listing1 = listing.get_all_listing();
        doctor = listing.objects.filter(category='1', status='p')
        hotels = listing.objects.filter(category='3', status='p')
        hospital = listing.objects.filter(category='5', status='p')
        gyms = listing.objects.filter(category='4', status='p')
        places = listing.objects.filter(category='5', status='p')
        # sports = listing.objects.filter(category='6', status='p')
        other = listing.objects.filter(category='9', status='p')
        data = {'listing1': listing1, 'lcategories': list_categories,  'doctor': doctor, 'hospital': hospital, 'gyms': gyms, 'hotels': hotels, 'places': places}
        return render(request, 'index2.html', data)

def cat_listing(request, pk):
    list_categories = Category.objects.all()
    # name = listing.objects.filter(category=pk).second()
    listing_category = listing.objects.filter(category=pk, status='p')
    return render(request, 'listing_cat.html', {'listing': listing_category, 'lcategories': list_categories})

class ListDetailView(DetailView):
    model = listing
    template_name = 'listing_detail.html'

class UpdateListingView(UpdateView):
    model = listing
    template_name = 'listing/update_listing.html'
    fields = ['title', 'category', 'sub_category', 'lister_name', 'cno', 'email', 'address', 'city', 'Pin', 'description', 'image', 'open_time', 'close_time']

class DeleteListingView(DeleteView):
    model = listing
    template_name = 'listing/delete_listing.html'
    success_url = reverse_lazy('profile')

@login_required
def AddlistingView(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           # Get the current instance object to display in the template
           img_obj = form.instance
           return render(request, 'listing_response.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ListingForm()
    return render(request, 'listing/add_listing.html', {'form': form})


class UpdateListingView(UpdateView):
    model = listing
    template_name = 'listing/update_listing.html'
    fields = ['title', 'category', 'sub_category', 'lister_name', 'cno', 'email', 'address', 'city', 'Pin', 'description', 'image', 'open_time', 'close_time']

def listing_cat(request):
    cat = Sub_Category.get_all_cat()
    return render(request, 'listing_cat1.html', {'cat': cat})

def show(request):
    x = listing1.objects.all()
    x2 = Category.objects.all()
    return render(request, 'listing/listing.html', {'x': x, 'x2': x2})

def cat(request, id):
    x = listing1.objects.filter(id='<int:id>')
    return render(request, 'listing/listing.html', {'x': x, 'x2': x2})

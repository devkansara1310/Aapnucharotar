from django.shortcuts import render
from .models import offers, Categoryoffers
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from offer.forms import OfferForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.

def offers1(request):
    offercategories = Categoryoffers.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        offer1 = offers.get_all_offers_by_id(categoryID)
        data1 = {'offer1': offer1, 'offerscategories': offercategories}
        return render(request, 'offer_cat.html', data1)
    else:
        offer1 = offers.get_all_offers();
        data = {'offer1': offer1, 'offerscategories': offercategories}
        return render(request, 'index3.html', data)

def cat_offer(request, pk):
    offer_categories = Categoryoffers.objects.all()
    # name = listing.objects.filter(category=pk).second()
    offer_category = offers.objects.filter(Category=pk, status='p')
    return render(request, 'offer_cat.html', {'offer': offer_category, 'ocategories': offer_categories})


class OfferDetailView(DetailView):
    model = offers
    template_name = 'offer_detail.html'

class UpdateOfferView(UpdateView):
    model = offers
    template_name = 'offer/update_offer.html'
    fields = ['name', 'code', 'image', 'Description', 'end', 'Category', 'Contact', 'email', 'address', 'city']

class DeleteOffersView(DeleteView):
    model = offers
    template_name = 'offer/delete_offer.html'
    success_url = reverse_lazy('profile')

@login_required
def AddofferView(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           # Get the current instance object to display in the template
           img_obj = form.instance
           return render(request, 'offer_response.html', {'form': form, 'img_obj': img_obj})
    else:
        form = OfferForm()
    return render(request, 'offer/add_offer.html', {'form': form})

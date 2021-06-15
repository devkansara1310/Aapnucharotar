from django.urls import path
from . import views
from .views import OfferDetailView, AddofferView,UpdateOfferView, DeleteOffersView, cat_offer

urlpatterns = [
   path('', views.offers1, name='offers'),
   path('category/<int:pk>', views.cat_offer, name='offer_cat'),
   path('offer/<int:pk>', OfferDetailView.as_view(), name='offer_detail'),
   path('add_offer/', views.AddofferView, name='add_offer'),
   path('edit/<int:pk>', UpdateOfferView.as_view(), name='update_offer'),
   path('delete/<int:pk>', DeleteOffersView.as_view(), name='delete_offer'),
   # path('category/<int:id>', views.show, name='cat'),
   # path('cat', views.listing_cat,name='cat'),
]

from django.urls import path
from . import views

urlpatterns = [
   path('', views.Donation,name='donation'),
   path('donation/', views.donationhome,name='donation1'),
   path('handlerequest/', views.hendlerequest, name='HandleRequest'),


]

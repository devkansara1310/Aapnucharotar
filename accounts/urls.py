from django.urls import path
from .import views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('customer_register/',views.customer_register, name='customer_register'),
     path('blogger_register/',views.blogger_register, name='blogger_register'),
     path('lister_register/',views.lister_register, name='lister_register'),
     path('vendor_register/',views.vendor_register, name='vendor_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]

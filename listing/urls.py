from django.urls import path
from . import views
from .views import ListDetailView, AddlistingView, UpdateListingView,cat_listing, DeleteListingView

urlpatterns = [
   path('', views.listing01, name='listing'),
   path('<int:pk>', ListDetailView.as_view(), name='list_detail'),
   path('add_list', views.AddlistingView, name='add_listing'),
   path('edit/<int:pk>', UpdateListingView.as_view(), name='update_listing'),
   path('delete/<int:pk>', DeleteListingView.as_view(), name='delete_listing'),
   # path('add_post/', AddPostView.as_view(), name='addpost')
   # path('category/<int:id>', views.show, name='cat'),
   path('category/<int:pk>', views.cat_listing, name='listing_cat'),
]

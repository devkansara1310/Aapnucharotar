from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('',blog1.as_view(),name='blog1'),
    # path("register",views.register_request,name="register"),
    # path('add_post/', AddPostView.as_view(), name='addpost')
    # path('<int:id>', views.show, name='show'),
    # path('', blog.as_view(), name="blog1"),
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('profile/', views.test, name="profile"),
    # path('upload/', views.image_upload_view),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('category/<int:pk>', views.cat_blog, name='blog_cat'),
    path('blogger/add_post/', views.AddPostView, name='add_post'),
    # path('article/<int:_id>', views.BlogDetailView, name='article_detailview'),
    # path('add_post/', AddPostView.as_view(), name='add_post'),
    path('blog/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('like/<int:pk>', BlogPostLike, name="like_post"),
    path('comment/<int:_id>', Comment, name='blog'),
    path('blog/<int:pk>/comment/', CommentView.as_view(), name='add_comment'),

]

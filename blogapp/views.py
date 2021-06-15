from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DetailView, DeleteView, ListView
from .models import Post, Comment, Category
from listing.models import listing
from offer.models import offers
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


def test(request):
    posts = Post.get_all_blog_d()
    posts_count = Post.get_all_blog_d().count()
    listing1 = listing.get_listing()
    listing1_count = listing.get_listing().count()
    offer1 = offers.get_offer()
    offer1_count = offers.get_offer().count()
    return render(request, '1.html', {'posts': posts,'posts_count': posts_count,'listing1_count': listing1_count,'listing1': listing1, 'offer1': offer1,  'offer1_count': offer1_count})

def index(request):
    listing1 = listing.get_all_listing()
    posts = Post.get_all_blog()
    offer = offers.get_all_offers()
    data = {'posts': posts, 'listing1': listing1,'offer': offer}
    return render(request, 'index.html', data)

@login_required
def BlogPostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user.id)
    # if post.likes.filter(id=request.user.id).exists():
    #     post.likes.remove(request.user)
    # else:
    #     post.likes.add(request.user)

    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))


def blog(request):
    # Post = None
    categories = Category.objects.all()
    listing1 = listing.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        posts = Post.get_all_blog_by_id(categoryID)
        data1 = {'posts': posts,  'categories': categories}
        return render(request, 'blog_cat.html', data1)
    else:
        posts = Post.get_all_blog()
        news = Post.objects.filter(category='2', status='p')
        food = Post.objects.filter(category='1', status='p')
        events = Post.objects.filter(category='3', status='p')
        entertainment = Post.objects.filter(category='4', status='p')
        places = Post.objects.filter(category='5', status='p')
        sports = Post.objects.filter(category='6', status='p')
        other = Post.objects.filter(category='7', status='p')
        data = {'posts': posts, 'categories': categories, 'listing': listing1, 'news': news, 'food': food, 'events': events, 'entertainment': entertainment, 'places': places, 'sports': sports,'other': other}
        return render(request, 'index1.html', data)

def cat_blog(request, pk):
    blog_categories = Category.objects.all()
    # name = listing.objects.filter(category=pk).second()
    blog_category = Post.objects.filter(category=pk, status='p')
    return render(request, 'blog_cat.html', {'blog': blog_category, 'bcategories': blog_categories})


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"]= total_likes
        return context

#comments
class CommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html'
    # fields = '__all__'
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('blog')


@login_required
def AddPostView(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           # Get the current instance object to display in the template
           img_obj = form.instance
           return render(request, 'blog_response.html', {'form': form, 'img_obj': img_obj})
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})


    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #
    #     likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
    #     liked = False
    #     if likes_connected.likes.filter(id=self.request.user.id).exists():
    #         liked = True
    #     data['number_of_likes'] = likes_connected.number_of_likes()
    #     data['post_is_liked'] = liked
    #     return data

#
# def BlogDetailView(request, _id):
#     try:
#         data = Post.objects.get(id=_id)
#         comments = CommentModel.objects.filter(blog=data)
#     except Post.DoesNotExist:
#         raise Http404('Data does not exist')
#
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             Comment = CommentModel(your_name=form.cleaned_data['your_name'],
#                                    comment_text=form.cleaned_data['comment_text'],
#                                    blog=data)
#             Comment.save()
#             return redirect('article/<int:id>')
#     else:
#         form = CommentForm()
#
#     context = {
#         'data': data,
#         'form': form,
#         'comments': comments,
#     }
#     return render(request, 'blog/article_details.html', context)
#

# class AddPostView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'blog/add_post.html'
#
#
# def image_upload_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'add_post.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = PostForm()
#     return render(request, 'add_post.html', {'form': form})
#
#
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    fields = ['title', 'description', 'image', 'category', 'sub_category']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('test')

def detail(request):
    return render(request, 'listing_detail.html')

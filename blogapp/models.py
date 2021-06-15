from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from accounts.models import customer, User

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]

class Category(models.Model):
    name = models.CharField('Category', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    add = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

def get_first_User():
    return [User.objects.first().pk]

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/', null=True, verbose_name="")
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog')

    @staticmethod
    def get_all_blog_d():
        return Post.objects.filter(status='p')

    @staticmethod
    def get_all_blog():
        return Post.objects.filter(status='p').order_by('id')[:8]

    @staticmethod
    def get_all_blog_by_id(category_id):
        if category_id:
            return Post.objects.filter(category=category_id)
        else:
            x1 = Post.objects.filter(status='p')
            return x1

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title



    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

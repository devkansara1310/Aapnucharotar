from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
             'author': forms.TextInput(attrs={'id': 'user', 'type': 'hidden'}),
             'likes': forms.TextInput(attrs={'type': 'hidden'}),
             'status': forms.TextInput(attrs={'id': 'status', 'type': 'hidden'})
        }





#
# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")
#
#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user
#

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'description', 'image', 'author', 'category', 'sub_category')
#
#         widget = {
#             'title ': forms.TextInput(attrs={'class': 'form-control'}),
#             'description ': forms.TextInput(attrs={'class': 'form-control'}),
#             'image ': forms.ImageField(),
#             'author': forms.TextInput(attrs={'class': 'form-control', 'id1':'panthi'}),
#             'category ': forms.Select(attrs={'class': 'form-control'}),
#             'sub_category ': forms.Select(attrs={'class': 'form-control'}),
#            # 'author ': forms.Select(attrs={'class': 'form-control'}),
#
#
#         }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widget = {
            'name ': forms.TextInput(attrs={'class': 'form-control'}),
            'body ': forms.Textarea(attrs={'class': 'form-control'}),
        }

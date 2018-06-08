from django import forms
from django.contrib.auth.models import User
from . models import Post




#create forms here 

class IndexForm(forms.ModelForm):
    post = forms.ImageField()

    


class CreatePostForm(forms.ModelForm): 

    class Meta:
        model = Post
        fields = ('caption', 'postpic',)
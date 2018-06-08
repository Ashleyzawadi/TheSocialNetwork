from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CreatePostForm, IndexForm
from .models import Post


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        form = IndexForm()
        args = {'form': form}
        posts = Post.objects.all()

        args = {'form': form, 'posts': posts,}
        return render(request, self.template_name, args) 

    def post(self, request):
        form = IndexForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()

            form = HomeForm()
            return redirect('insta:index')

            args = {'form': form, 'post': post}
            return render(request, self.template_name, args)












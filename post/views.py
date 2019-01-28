from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from.forms import PostModelForm

# Create your views here.

def index(request):
    context = {}
    post = Post.objects.all()
    context['posts'] = post
    return render(request, 'index.html', context)


def detail(request, post_id):
    context = {}
    context['post'] = post.objects.get(id=post_id)
    return render (request, 'detail.html', context)


def create(request):
        context = {}

        if request.method == 'POST':
            form = PostModelForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('post:index')
            else:
                context['form'] = form
                return render(request, 'create.html', context)

        else:
            context['form'] = PostModelForm()
            return render(request, 'create.html', context)


def update(request, post_id):
    context = {}
    post = post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponse('Post Updated')
        else:
            context['form'] = form
            render(request, 'update.html', context)

    else:
        context['form'] = PostModelForm(instance=post)
    return render(request, 'update.html', context)



def comment(request):
    return render(request, 'detail.html', context)

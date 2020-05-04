from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from ..forms import PostForm
from ..models import Post


class CreatePostView(View):
    def get(self, request):
        if not request.user.is_staff:
            raise Http404('Not found')

        form = PostForm()
        return render(request, 'webapp/create_post.html', {'form': form})

    def post(self, request):
        if not request.user.is_staff:
            raise Http404('Not found')

        form = PostForm(request.POST)
        if form.is_valid():
            p = Post()
            p.title = form.cleaned_data['title']
            p.content = form.cleaned_data['content']
            p.save()
            return redirect('webapp:index')

        return render(request, 'webapp/create_post.html', {'form': form})


class DeletePostView(View):
    def get(self, request, post_id):
        if not request.user.is_staff:
            raise Http404('Not found')

        post = get_object_or_404(Post, pk=post_id)
        post.delete()

        return redirect('webapp:index')


class EditPostView(View):
    def get(self, request, post_id):
        if not request.user.is_staff:
            raise Http404('Not found')

        post = get_object_or_404(Post, pk=post_id)
        form = PostForm(instance=post)

        return render(request, 'webapp/create_post.html', {'form': form})

    def post(self, request, post_id):
        if not request.user.is_staff:
            raise Http404('Not found')

        post = get_object_or_404(Post, pk=post_id)
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()

        return redirect('webapp:index')


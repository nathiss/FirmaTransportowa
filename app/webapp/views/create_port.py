from django.views import View
from django.shortcuts import render, redirect
from django.http import Http404

from ..forms import CreatePortForm
from ..models import Post


class CreatePostView(View):
    def get(self, request):
        if not request.user.is_staff:
            raise Http404('Not found')

        form = CreatePortForm()
        return render(request, 'webapp/create_post.html', {'form': form})

    def post(self, request):
        if not request.user.is_staff:
            raise Http404('Not found')

        form = CreatePortForm(request.POST)
        if form.is_valid():
            p = Post()
            p.title = form.cleaned_data['title']
            p.content = form.cleaned_data['content']
            p.save()
            return redirect('webapp:index')

        return render(request, 'webapp/create_post.html', {'form': form})

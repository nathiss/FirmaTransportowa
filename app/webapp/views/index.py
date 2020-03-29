from django.views import View
from django.shortcuts import render

from ..models import Post


class IndexView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.order_by('-datetime')
        return render(request, 'webapp/index.html', {"posts": posts})

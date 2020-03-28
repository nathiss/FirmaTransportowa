from django.views import View
from django.shortcuts import render, get_object_or_404, redirect


class IndexView(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'webapp/index.html')

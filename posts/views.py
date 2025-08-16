from django.views.generic import (
    TemplateView,
    ListView
    )
from django.http import HttpResponse
from django.shortcuts import render 
from .models import Post, Status
# Create your views here.
class HomePageView(TemplateView):
    template_name = "posts/delete.html"

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    context_objext_name = "post_list"

    def get_queryset(self):
        status = Status.objects.get(name="published")
        return Post.objects.filter(status=status).order_by("created_on").reverse()
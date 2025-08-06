from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render 
# Create your views here.
class HomePageView(TemplateView):
    template_name = "pages/home.html"

def about(request):
   return render(request, 'pages/about.html')


from django.urls import path
from .views import HomePageView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('home/', HomePageView.as_view(), name="homeTwo"),
    path('about/', views.about, name='about'),
]
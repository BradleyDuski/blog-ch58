from django.urls import path
from . import views  # This imports accounts/views.py
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('accounts/', views.index, name='account_home'),  # Looks for 'index' in views
      path('login/', auth_views.LoginView.as_view(), name='login'),
]


from django.contrib import admin
from django.urls import path, include
from posts.views import PostCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
      path('posts/', include('posts.urls')),
      path('accounts/', include("accounts.urls")),
      #path('accounts/', include("django.contrib.auth.urls")),
      path('new/', PostCreateView.as_view(), name='post_new'),
      path('accounts/', include("allauth.urls")),
]
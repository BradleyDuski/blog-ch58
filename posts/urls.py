from django.urls import path
from .views import  (HomePageView,
                     PostListView,
                     PostCreateView,
                     PostDetailView,
                     PostDeleteView,
                     PostUpdateView
                     )
from django.urls import reverse_lazy


urlpatterns = [
    path('posts/', HomePageView.as_view(), name="posts"),
    path("list/", PostListView.as_view(), name="post_list"),
    path('new/', PostCreateView.as_view(), name="new_post"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit")
    

]
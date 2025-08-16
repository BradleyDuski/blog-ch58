from django.urls import path
from .views import  (HomePageView,
                     PostListView
                     )


urlpatterns = [
    path('posts/', HomePageView.as_view(), name="posts"),
    path("list/", PostListView.as_view(), name="post_list")

]
from django.urls import path
from .views import PostListView, PostDetailView, Posts_by_Category, Posts_by_Tag

app_name = 'blog'

urlpatterns = [
  path('', PostListView.as_view(), name='post_list'),
  path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
  path('category/<str:slug>', Posts_by_Category.as_view(), name='posts_by_category'),
  path('tags/<slug:slug>', Posts_by_Tag.as_view(), name='posts_by_tag'),
]
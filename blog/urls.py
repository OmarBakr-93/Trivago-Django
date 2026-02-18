from django.urls import path
from .views import PostListView, PostDetailView, Posts_by_Category, Posts_by_Tag
from .api_view import post_list_api, post_detail_api, post_search_api

app_name = 'blog'

urlpatterns = [
  path('', PostListView.as_view(), name='post_list'),
  path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
  path('category/<str:slug>', Posts_by_Category.as_view(), name='posts_by_category'),
  path('tags/<slug:slug>', Posts_by_Tag.as_view(), name='posts_by_tag'),
  
  # api
  path('api_list/', post_list_api, name='post_list_api'),
  path('api_detail/<int:id>', post_detail_api, name='post_detail_api'),
  path('api_search/<str:query>', post_search_api, name='post_search_api'),
]
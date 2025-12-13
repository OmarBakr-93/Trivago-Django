from django.urls import path
from . import views


app_name = 'settings'

urlpatterns = [
  path('', views.home, name='home'),
  path('search/', views.home_search, name='home_search'),
  path('contact/', views.contact, name='contact'),
  path('category/<slug:category>', views.category_filter, name='category_filter'),
]

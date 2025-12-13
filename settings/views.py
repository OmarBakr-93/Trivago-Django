from django.shortcuts import render
from property.models import Property, Place, Category
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post
from django.contrib.auth.models import User
from .models import Settings

# Create your views here.


def home(request):
  
  places = Place.objects.all().annotate(properties_count=Count('property_place'))
  categories = Category.objects.all()
  
  restaurant_list = Property.objects.filter(category__name='Restaurant')[:5]
  hotels_list = Property.objects.filter(category__name='hotels')[:4]
  places_list = Property.objects.filter(category__name='places')[:5]
  
  recent_posts = Post.objects.all()[:4]
  
  users_count = User.objects.count()
  places_count =Property.objects.filter(category__name='places').count() 
  hotels_count =Property.objects.filter(category__name='hotels').count()
  restaurant_count =Property.objects.filter(category__name='Restaurant').count()
  
  return render(request, 'settings/home.html',{
    'places': places,
    'categories': categories,
    'restaurant_list': restaurant_list,
    'hotels_list': hotels_list,
    'places_list': places_list,
    'recent_posts': recent_posts,
    'users_count': users_count,
    'places_count': places_count,
    'hotels_count': hotels_count,
    'restaurant_count': restaurant_count,
  })
  
  
def home_search(request):
  name = request.GET.get('name') 
  place = request.GET.get('place')
  
  property_list = Property.objects.filter(Q(name__icontains=name) & Q(place__name__icontains=place))
  
  return render(request, 'settings/home_search.html', {
    'property_list': property_list,
  })


def category_filter(request, category):
  category = Category.objects.get(name=category) 
  property_list = Property.objects.filter(category=category)
  
  return render(request, 'settings/home_search.html', {
    'property_list': property_list
  })
  
  
def contact(request):
  data = Settings.objects.last()
  return render(request, 'settings/contact.html',{
    'data': data
  })
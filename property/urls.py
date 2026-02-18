from django.urls import path
from .views import PropertyList, PropertyDetail
from .api_view import PropertyApiList, PropertyApiDetail

app_name = 'property'



urlpatterns = [
  path('', PropertyList.as_view(), name='property_list'),
  path('<slug:slug>', PropertyDetail.as_view(), name='property_detail'),
  
  # api 
  
  path('api_list/', PropertyApiList.as_view(), name='property_list_api'),
  path('api_detail/<int:pk>/', PropertyApiDetail.as_view(), name='property_detail_api'),
  
]
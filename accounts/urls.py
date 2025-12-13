from django.urls import path
from .views import signup, profile, profile_edit, MyReservations, MyListings

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('reservation/', MyReservations, name='reservation'),
    path('mylistings/', MyListings, name='mylistings'),
]
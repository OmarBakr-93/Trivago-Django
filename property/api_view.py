from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PropertySerializer
from .models import Property
from rest_framework.permissions import IsAuthenticated


class PropertyApiList(ListCreateAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer
  permission_classes = [IsAuthenticated]
  
  
  
class PropertyApiDetail(RetrieveUpdateDestroyAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer
  permission_classes = [IsAuthenticated]
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Property(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='property_owner')
  name = models.CharField(max_length=100, unique=True)
  main_images = models.ImageField(upload_to='property/')
  price = models.IntegerField(default=0)
  description = models.TextField(max_length=10000)
  place = models.ForeignKey('Place', related_name='property_place',on_delete=models.CASCADE)
  category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='property_category')
  created_at = models.DateTimeField(auto_now_add=True)
  slug = models.SlugField(blank=True, null=True)
  
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
      super(Property, self).save(*args, **kwargs)
      
      
  def get_absolute_url(self):
      return reverse("property:property_detail", kwargs={"slug": self.slug})

      
  def __str__(self):
    return self.name

class property_images(models.Model):
  property = models.ForeignKey(Property, related_name='property_images' ,on_delete=models.CASCADE)
  images = models.ImageField(upload_to='propertyImages/')
  
  def __str__(self):
    return str(self.property)
  
class Place(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='places/')
  
  def __str__(self):
    return self.name
  
class Category(models.Model):
  name = models.CharField(max_length=40)
  icon = models.CharField(max_length=40)
  def __str__(self):
    return self.name
  
  
class Property_Review(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')
  property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_review')
  rate = models.IntegerField(default=0)
  feedback = models.TextField(max_length=2000)
  created_at = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return str(self.property)
  
  
count = (
  (1, '1'),
  (2, '2'),
  (3, '3'),
  (4, '4'),
  (5, '5'),
)
class Property_book(models.Model):
  property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_book')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_owner')
  date_from = models.DateField(default=timezone.now)
  date_to = models.DateField(default=timezone.now)
  guest = models.IntegerField(choices=count)
  children = models.IntegerField(choices=count)
  
  def __str__(self):
    return str(self.property)
from django.db import models

# Create your models here.

class Settings(models.Model):
  site_name = models.CharField(max_length=50)
  logo = models.ImageField(upload_to='settings/')
  phone = models.CharField(max_length=20)
  email = models.EmailField()
  address = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  facebook_link = models.URLField()
  instagram_link = models.URLField()
  twitter_link = models.URLField()

  def __str__(self):
    return self.site_name
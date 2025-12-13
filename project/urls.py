
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path('admin/', admin.site.urls),
    path('property/', include('property.urls', namespace='property')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('summernote/', include('django_summernote.urls')),
    path('',include('settings.urls', namespace='home')),
    path('about/', include('about.urls', namespace='about')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.       MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
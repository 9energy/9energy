from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('about', include("about.urls")),
    path('service', include("service.urls")),
    path('contactus', include("contactus.urls")),
    path('gallery', include("gallery.urls")),
    path('product', include("product.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

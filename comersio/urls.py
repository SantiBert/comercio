from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
    path('', include('social.urls')),
    path('', include('domicilio.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

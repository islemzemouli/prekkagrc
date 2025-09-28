from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # core.urls must be
    path("services/", include("services.urls")),
    path('blog/', include('blog.urls')),  # toutes les URLs de l'app blog
    path('realisations/', include('realisations.urls')),
    path('contact/', include('contact.urls')),
    path("users/", include("users.urls")),


]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Administration Prekka GRC"
admin.site.site_title = "Prekka GRC Admin"
admin.site.index_title = "Bienvenue dans le panneau d’administration"

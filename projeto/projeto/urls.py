from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'usuario/', include('usuario.urls')),
    url(r'unidade/', include('unidade.urls')),
    url(r'triagem/', include('triagem.urls')),
   
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
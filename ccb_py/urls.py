from django.urls import path, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('ccb_py.core.urls')),
    path('conta/', include('ccb_py.accounts.urls')),
    path('clientes/', include('ccb_py.clientes.urls')),
    #path('fornecedores/', include('ccb_py.fornecedores.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
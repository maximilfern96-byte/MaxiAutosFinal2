from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.inicio, name='inicio'),

    path('vehiculos/', views.lista_vehiculos, name='vehiculos'),

    path('categoria/<slug:slug>/', views.vehiculos_por_categoria, name='vehiculos_categoria'),

    path('vehiculo/<int:vehiculo_id>/', views.detalle_vehiculo, name='detalle_vehiculo'),

    path('favorito/<int:vehiculo_id>/', views.agregar_favorito, name='agregar_favorito'),

    path('quitar_favorito/<int:vehiculo_id>/', views.quitar_favorito, name='quitar_favorito'),

    path('favoritos/', views.mis_favoritos, name='mis_favoritos'),

    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
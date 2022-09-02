from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CarroViewSet, CategoriaViewSet, MarcaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'marca', MarcaViewSet)
router.register(r'marca', CarroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
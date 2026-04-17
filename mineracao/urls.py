from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpresaViewSet, PatenteViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'patentes', PatenteViewSet)

urlpatterns = [
    path('', include(router.urls))
]

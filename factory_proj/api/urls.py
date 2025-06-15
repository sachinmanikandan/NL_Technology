from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import (
    ManViewSet, MethodViewSet, MachineViewSet, MaterialViewSet,
    MethodListCreateAPIView
)

router = DefaultRouter()
router.register(r'mans_api', ManViewSet)
router.register(r'methods_api', MethodViewSet)
router.register(r'machines_api', MachineViewSet)
router.register(r'materials_api', MaterialViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search-methods/', MethodListCreateAPIView.as_view(), name='api-method-search'),
]

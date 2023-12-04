from django.urls import path, include
from rest_framework import routers
from main.views import NetworkViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'network', NetworkViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

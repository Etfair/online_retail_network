from rest_framework import viewsets, filters, permissions
from .models import Network, Product
from .permissions import IsActiveEmployee
from .serializers import NetworkSerializer, ProductSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [permissions.IsAuthenticated, IsActiveEmployee]
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

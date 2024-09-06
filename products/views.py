from django.shortcuts import render, get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Product
from .serializers import (
    ProductSerializer,
    ListProductSerializer,
    ProductDetailSerializer,
)


class ProductListView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all().order_by("-pk")
    serializer_class = ListProductSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ProductDetailView(RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "pk"

    def get_object(self):
        return get_object_or_404(self.queryset, pk=self.kwargs["pk"])

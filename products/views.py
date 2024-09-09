from gc import get_objects

from django.shortcuts import render, get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    BasePermission,
)
from .models import Product
from .serializers import (
    ProductSerializer,
    ListProductSerializer,
)


class ProductListView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all().order_by("-pk")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListProductSerializer
        if self.request.method == "POST":
            return ProductSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(f"Request User: {request.user}, Author: {obj.author}")
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return obj.author == request.user


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

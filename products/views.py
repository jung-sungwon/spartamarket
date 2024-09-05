from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Product
from .serializers import ProductSerializer, ListProductSerializer
from rest_framework.permissions import IsAuthenticated


class ProductListView(ListAPIView):
    queryset = Product.objects.all().order_by("-pk")
    serializer_class = ListProductSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get_object(self):
        return get_object_or_404(self.queryset, pk=self.kwargs["pk"])


class CreateProductView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

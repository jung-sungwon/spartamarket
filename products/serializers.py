from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Product
        fields = "__all__"


class ListProductSerializer(ProductSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("content")
        ret.pop("create_at")
        return ret

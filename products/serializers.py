from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ListProductSerializer(ProductSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["author"] = instance.author.username
        ret.pop("content")
        ret.pop("image")
        ret.pop("create_at")
        ret.pop("id")

        return ret


class ProductDetailSerializer(ProductSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["author"] = instance.author.username
        ret.pop("id")

        return ret

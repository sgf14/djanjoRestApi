from rest_framework import serializers
from .models import product

# serializer will format into proper json
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ["id", "part_no", "product_desc", "product_cost"]
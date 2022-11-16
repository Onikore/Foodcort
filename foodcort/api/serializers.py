from rest_framework import serializers

from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = (
            'name', 'price', 'type_id',
            'calories', 'proteins', 'fats',
            'carbohydrates', 'cooking_time', 'img_path'
        )

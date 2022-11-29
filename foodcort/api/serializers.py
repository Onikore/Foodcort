from rest_framework import serializers

from .models import Food, Sales, Ingredients, FoodType, Restaurants, Malls


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ('name',)


class FoodSerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True)
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Food
        fields = (
            'id', 'name', 'price', 'weight',
            'calories', 'proteins', 'fats',
            'carbohydrates', 'ingredients', 'type', 'cooking_time', 'description',
            'food_pic',
        )


class RestaurantsSerializer(serializers.ModelSerializer):
    food = FoodSerializer(many=True)

    class Meta:
        model = Restaurants
        fields = ('id', 'name', 'opening',
                  'closing', 'lat', 'lon',
                  'description', 'max_price', 'min_price',
                  'rating', 'food', 'rest_pic',)


class MallSerializer(serializers.ModelSerializer):
    restaurants = RestaurantsSerializer(many=True)

    class Meta:
        model = Malls
        fields = ('id', 'name', 'lat1',
                  'lon1', 'lat2', 'lon2',
                  'restaurants')


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

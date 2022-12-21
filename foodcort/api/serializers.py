from rest_framework import serializers

from .models import Food, Ingredients, FoodType, Restaurants, Malls, Status, Sales, SaleDetails


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('name',)

    def to_representation(self, instance):
        return str(instance)


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ('name',)

    def to_representation(self, instance):
        return str(instance)


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
                  'rating', 'rest_pic', 'floor', 'mall', 'food',)


class MallSerializer(serializers.ModelSerializer):
    restaurants = RestaurantsSerializer(many=True)

    class Meta:
        model = Malls
        fields = ('id', 'name', 'lat1',
                  'lon1', 'lat2', 'lon2',
                  'restaurants')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('name',)

    def to_representation(self, instance):
        return str(instance)


class SaleDetailsSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)

    class Meta:
        model = SaleDetails
        fields = ('food', 'amount',)


class SalesSerializer(serializers.ModelSerializer):
    # restaurant = RestaurantsSerializer()

    status = StatusSerializer()
    details = SaleDetailsSerializer(many=True, source='saledetails_set')

    class Meta:
        model = Sales
        fields = ('id', 'date_time', 'deadline',
                  'price', 'restaurant_id', 'status',
                  'user_id', 'details')

from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Food, Restaurants, Menu


class GetAllFood(APIView):
    def get(self, request):
        all_food = list(Food.objects.all().values().order_by('id'))
        restaurants = list(Restaurants.objects.all().values().order_by('id'))
        for i in restaurants:
            i['food'] = []
        menu = Menu.objects.all().values().order_by('id')
        for i in menu:
            restaurants[i['restaurant_id'] - 1]['food'].append(all_food[i['food_id'] - 1])
        return Response({'restaurants': restaurants})


class GetFoodImages(APIView):
    def get(self, request):
        # TODO: отправка JSON с картинками в виде BASE64
        #  пример
        #  "img_name" : "encoded_img"
        pass


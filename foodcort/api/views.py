import base64
from pathlib import Path

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Food, Restaurants, Menu


class GetAllFood(ListAPIView):
    def get(self, request, **kwargs):
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
        # Получается слишком тяжелый JSON
        # переписать так, чтобы отдавалось по 1 картинке
        res = {}
        for path in Path(r'C:\Users\Вип\Desktop\teamproject\foodcort\pictures').iterdir():
            with open(path, 'rb') as f:
                res[str(path.name)] = base64.b64encode(f.read())
        return Response(res)

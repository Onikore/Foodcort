import base64
from pathlib import Path

from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Food, Restaurants, Menu, Sales
from api.serializers import FoodSerializer, SalesSerializer


class GetFoodAPI(ListAPIView):
    serializer_class = FoodSerializer

    def get(self, request, **kwargs):
        all_food = Food.objects.all()
        if kwargs:
            return Response({'food': all_food.filter(id=kwargs.get('id')).values()})
        restaurants = list(Restaurants.objects.all().values().order_by('id'))
        for i in restaurants:
            i['food'] = []
        menu = Menu.objects.all().values().order_by('id')
        for i in menu:
            restaurants[i['restaurant_id'] - 1]['food'].append(all_food.filter(id=i['food_id']).values())
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


class GetSalesAPI(ListCreateAPIView):
    serializer_class = SalesSerializer

    def get(self, request, **kwargs):
        if kwargs:
            return Response({'sales': Sales.objects.all().filter(id=kwargs.get('id')).values()})
        return Response({'error': 'get request need sale id'})

    def post(self, request, *args, **kwargs):
        serializer = SalesSerializer(data=request.data)
        print(args, kwargs, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': 'something went wrong'})

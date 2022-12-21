from django.http import FileResponse
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Malls, Sales, Restaurants
from api.serializers import MallSerializer, SalesSerializer, RestaurantsSerializer


class GetFoodAPI(ListAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer


class GetMalls(ListAPIView):
    queryset = Malls.objects.all()
    serializer_class = MallSerializer

    # def get(self, request, **kwargs):
    #     req = Food.objects.all()
    #     if kwargs:
    #         return Response({'food': req.filter(id=kwargs.get('id')).values()})
    #     return Response({'restaurants': req.values()})


class GetFoodImages(APIView):
    def get(self, request, **kwargs):
        file_name = kwargs.get("name")
        try:
            return FileResponse(open(f'pictures/{file_name}', 'rb'))
        except FileNotFoundError:
            return Response({'error': 'FileNotFound'})


class GetSalesAPI(ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

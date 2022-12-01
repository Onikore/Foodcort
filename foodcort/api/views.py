from django.http import FileResponse
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Sales, Malls
from api.serializers import SalesSerializer, MallSerializer


class GetFoodAPI(ListAPIView):
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

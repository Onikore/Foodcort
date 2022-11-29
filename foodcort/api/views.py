import base64
from pathlib import Path

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

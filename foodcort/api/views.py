from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Food


# тестовые гет пост запросы
class BasicAPIView(APIView):
    def get(self, request):
        all_food = Food.objects.all().values()
        return Response({'food': list(all_food)})

    def post(self, request):
        return Response({'post': 'man'})

from django.contrib import admin
from django.urls import path

from api.views import GetAllFood, GetFoodImages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', GetAllFood.as_view()),
    path('api/v1/pictures/', GetFoodImages.as_view()),
]

from django.contrib import admin
from django.urls import path, include, re_path

from api.views import GetAllFood, GetFoodImages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/', GetAllFood.as_view()),
    path('api/v1/pictures/', GetFoodImages.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

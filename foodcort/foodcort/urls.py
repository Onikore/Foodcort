from django.contrib import admin
from django.urls import path, include, re_path

from api.views import GetFoodAPI, GetFoodImages, GetSalesAPI
from yasg_config import yasg_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/food/', GetFoodAPI.as_view()),
    path('api/v1/food/<int:id>/', GetFoodAPI.as_view()),
    path('api/v1/sales/', GetSalesAPI.as_view()),
    path('api/v1/sales/<int:id>/', GetSalesAPI.as_view()),
    path('pictures/<str:name>', GetFoodImages.as_view()),
    path('auth/v1/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
urlpatterns.extend(yasg_urls)

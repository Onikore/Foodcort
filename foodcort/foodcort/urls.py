from django.contrib import admin
from django.urls import path

from api.views import BasicAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', BasicAPIView.as_view()),
]

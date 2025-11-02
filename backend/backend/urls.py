from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('api/v1/', include('library.urls')),
    path('admin/', admin.site.urls),
]

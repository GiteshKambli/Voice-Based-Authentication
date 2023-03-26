from django.contrib import admin
from django.urls import path, include
from .views import FilesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('files', FilesViewSet, basename='files')

urlpatterns = [
    path('api/', include(router.urls)),
]


from django.urls import path, include
from rest_framework import routers
from ben10_app import views

router = routers.DefaultRouter()
router.register(r'aliens', views.AlienViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
